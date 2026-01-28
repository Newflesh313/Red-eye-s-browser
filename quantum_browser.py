"""
Quantum Browser - Standalone Desktop Web Browser
Built with Python + PyQt5 + QtWebEngine (Chromium)
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *

class BrowserTab(QWidget):
    """Individual browser tab with its own web view"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))
        
        # Layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.browser)
        
    def load_url(self, url):
        """Load a URL in this tab"""
        if not url.startswith('http'):
            url = 'https://' + url
        self.browser.setUrl(QUrl(url))
        
    def get_url(self):
        """Get current URL"""
        return self.browser.url().toString()
        
    def get_title(self):
        """Get current page title"""
        return self.browser.page().title()

class QuantumBrowser(QMainWindow):
    """Main browser window"""
    
    def __init__(self):
        super().__init__()
        
        # Window setup
        self.setWindowTitle("Quantum Browser")
        self.setGeometry(100, 100, 1200, 800)
        
        # Apply dark theme
        self.setup_theme()
        
        # Browser state
        self.tabs = []
        self.bookmarks = []
        self.history = []
        
        # Create UI
        self.create_ui()
        
        # Add first tab
        self.add_new_tab()
        
        # Set window icon
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_ComputerIcon))
        
    def setup_theme(self):
        """Apply dark theme to the browser"""
        dark_stylesheet = """
            QMainWindow {
                background-color: #0a0e1a;
            }
            QToolBar {
                background-color: #151b2e;
                border: none;
                padding: 5px;
                spacing: 5px;
            }
            QToolButton {
                background-color: #1e2a47;
                border: 1px solid #2d3748;
                border-radius: 5px;
                padding: 5px 10px;
                color: #e2e8f0;
                font-size: 13px;
            }
            QToolButton:hover {
                background-color: #2a3652;
                border-color: #6366f1;
            }
            QToolButton:pressed {
                background-color: #1e2a47;
            }
            QLineEdit {
                background-color: #1e2a47;
                border: 2px solid #2d3748;
                border-radius: 20px;
                padding: 8px 15px;
                color: #e2e8f0;
                font-size: 13px;
            }
            QLineEdit:focus {
                border-color: #6366f1;
            }
            QTabWidget::pane {
                border: none;
                background-color: #0a0e1a;
            }
            QTabBar::tab {
                background-color: #151b2e;
                color: #94a3b8;
                padding: 8px 20px;
                border-top-left-radius: 5px;
                border-top-right-radius: 5px;
                margin-right: 2px;
            }
            QTabBar::tab:selected {
                background-color: #1e2a47;
                color: #e2e8f0;
            }
            QTabBar::tab:hover {
                background-color: #2a3652;
            }
            QStatusBar {
                background-color: #151b2e;
                color: #94a3b8;
                border-top: 1px solid #2d3748;
            }
            QMenu {
                background-color: #1e2a47;
                color: #e2e8f0;
                border: 1px solid #2d3748;
            }
            QMenu::item:selected {
                background-color: #6366f1;
            }
        """
        self.setStyleSheet(dark_stylesheet)
        
    def create_ui(self):
        """Create the browser user interface"""
        
        # Navigation toolbar
        navbar = QToolBar("Navigation")
        navbar.setMovable(False)
        navbar.setIconSize(QSize(20, 20))
        self.addToolBar(navbar)
        
        # Back button
        back_btn = QAction("◀ Back", self)
        back_btn.setStatusTip("Go back")
        back_btn.triggered.connect(self.navigate_back)
        navbar.addAction(back_btn)
        
        # Forward button
        forward_btn = QAction("Forward ▶", self)
        forward_btn.setStatusTip("Go forward")
        forward_btn.triggered.connect(self.navigate_forward)
        navbar.addAction(forward_btn)
        
        # Reload button
        reload_btn = QAction("⟳ Reload", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(self.reload_page)
        navbar.addAction(reload_btn)
        
        # Home button
        home_btn = QAction("⌂ Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)
        
        navbar.addSeparator()
        
        # URL address bar
        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Search or enter website URL...")
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        
        navbar.addSeparator()
        
        # New tab button
        new_tab_btn = QAction("+ New Tab", self)
        new_tab_btn.setStatusTip("Open new tab")
        new_tab_btn.triggered.connect(self.add_new_tab)
        navbar.addAction(new_tab_btn)
        
        # Bookmarks button
        bookmark_btn = QAction("★ Bookmark", self)
        bookmark_btn.setStatusTip("Bookmark this page")
        bookmark_btn.triggered.connect(self.add_bookmark)
        navbar.addAction(bookmark_btn)
        
        # Downloads button
        downloads_btn = QAction("⬇ Downloads", self)
        downloads_btn.setStatusTip("Show downloads")
        downloads_btn.triggered.connect(self.show_downloads)
        navbar.addAction(downloads_btn)
        
        # Settings button
        settings_btn = QAction("⚙ Settings", self)
        settings_btn.setStatusTip("Browser settings")
        settings_btn.triggered.connect(self.show_settings)
        navbar.addAction(settings_btn)
        
        # Tab widget
        self.tabs_widget = QTabWidget()
        self.tabs_widget.setTabsClosable(True)
        self.tabs_widget.tabCloseRequested.connect(self.close_tab)
        self.tabs_widget.currentChanged.connect(self.current_tab_changed)
        self.setCentralWidget(self.tabs_widget)
        
        # Status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready")
        
    def add_new_tab(self):
        """Add a new browser tab"""
        new_tab = BrowserTab()
        
        # Connect signals
        new_tab.browser.urlChanged.connect(lambda url: self.update_url_bar())
        new_tab.browser.loadFinished.connect(lambda: self.update_title())
        new_tab.browser.loadProgress.connect(self.update_progress)
        
        # Add tab
        index = self.tabs_widget.addTab(new_tab, "New Tab")
        self.tabs_widget.setCurrentIndex(index)
        self.tabs.append(new_tab)
        
        # Update URL bar
        self.update_url_bar()
        
    def close_tab(self, index):
        """Close a tab"""
        if self.tabs_widget.count() > 1:
            self.tabs_widget.removeTab(index)
            self.tabs.pop(index)
        else:
            self.close()
            
    def current_tab_changed(self, index):
        """Handle tab change"""
        if index >= 0:
            self.update_url_bar()
            self.update_title()
            
    def get_current_tab(self):
        """Get the currently active tab"""
        return self.tabs_widget.currentWidget()
        
    def navigate_to_url(self):
        """Navigate to URL from address bar"""
        url = self.url_bar.text()
        
        if not url:
            return
            
        # Check if it's a search query or URL
        if ' ' in url or '.' not in url:
            # Search query
            url = f"https://www.google.com/search?q={url}"
        elif not url.startswith('http'):
            url = 'https://' + url
            
        current_tab = self.get_current_tab()
        if current_tab:
            current_tab.load_url(url)
            self.history.append(url)
            
    def update_url_bar(self):
        """Update URL bar with current page URL"""
        current_tab = self.get_current_tab()
        if current_tab:
            url = current_tab.get_url()
            self.url_bar.setText(url)
            
    def update_title(self):
        """Update window and tab title"""
        current_tab = self.get_current_tab()
        if current_tab:
            title = current_tab.get_title()
            self.setWindowTitle(f"{title} - Quantum Browser")
            
            # Update tab title
            index = self.tabs_widget.currentIndex()
            if len(title) > 20:
                title = title[:20] + "..."
            self.tabs_widget.setTabText(index, title)
            
    def update_progress(self, progress):
        """Update loading progress"""
        if progress < 100:
            self.status_bar.showMessage(f"Loading... {progress}%")
        else:
            self.status_bar.showMessage("Done")
            
    def navigate_back(self):
        """Go back in history"""
        current_tab = self.get_current_tab()
        if current_tab:
            current_tab.browser.back()
            
    def navigate_forward(self):
        """Go forward in history"""
        current_tab = self.get_current_tab()
        if current_tab:
            current_tab.browser.forward()
            
    def reload_page(self):
        """Reload current page"""
        current_tab = self.get_current_tab()
        if current_tab:
            current_tab.browser.reload()
            
    def navigate_home(self):
        """Navigate to home page"""
        current_tab = self.get_current_tab()
        if current_tab:
            current_tab.load_url("https://www.google.com")
            
    def add_bookmark(self):
        """Add current page to bookmarks"""
        current_tab = self.get_current_tab()
        if current_tab:
            url = current_tab.get_url()
            title = current_tab.get_title()
            
            if url not in self.bookmarks:
                self.bookmarks.append(url)
                QMessageBox.information(self, "Bookmark Added", 
                                       f"Added to bookmarks:\n{title}")
            else:
                QMessageBox.information(self, "Already Bookmarked", 
                                       "This page is already bookmarked")
                                       
    def show_downloads(self):
        """Show downloads dialog"""
        QMessageBox.information(self, "Downloads", 
                               "Downloads feature coming soon!\n\nDownloads will be saved to your Downloads folder.")
                               
    def show_settings(self):
        """Show settings dialog"""
        dialog = QDialog(self)
        dialog.setWindowTitle("Browser Settings")
        dialog.setGeometry(200, 200, 400, 300)
        
        layout = QVBoxLayout()
        
        # Settings info
        info_label = QLabel("Quantum Browser v1.0")
        info_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #6366f1;")
        layout.addWidget(info_label)
        
        layout.addWidget(QLabel("\nSettings:\n"))
        
        # Home page setting
        home_layout = QHBoxLayout()
        home_layout.addWidget(QLabel("Home Page:"))
        home_input = QLineEdit("https://www.google.com")
        home_layout.addWidget(home_input)
        layout.addLayout(home_layout)
        
        layout.addStretch()
        
        # Buttons
        btn_layout = QHBoxLayout()
        save_btn = QPushButton("Save")
        save_btn.clicked.connect(dialog.accept)
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(dialog.reject)
        btn_layout.addWidget(save_btn)
        btn_layout.addWidget(cancel_btn)
        layout.addLayout(btn_layout)
        
        dialog.setLayout(layout)
        dialog.exec_()
        
    def keyPressEvent(self, event):
        """Handle keyboard shortcuts"""
        # Ctrl+T - New tab
        if event.key() == Qt.Key_T and event.modifiers() == Qt.ControlModifier:
            self.add_new_tab()
            
        # Ctrl+W - Close tab
        elif event.key() == Qt.Key_W and event.modifiers() == Qt.ControlModifier:
            current_index = self.tabs_widget.currentIndex()
            self.close_tab(current_index)
            
        # Ctrl+L - Focus address bar
        elif event.key() == Qt.Key_L and event.modifiers() == Qt.ControlModifier:
            self.url_bar.setFocus()
            self.url_bar.selectAll()
            
        # Ctrl+R or F5 - Reload
        elif (event.key() == Qt.Key_R and event.modifiers() == Qt.ControlModifier) or event.key() == Qt.Key_F5:
            self.reload_page()
            
        # Alt+Left - Back
        elif event.key() == Qt.Key_Left and event.modifiers() == Qt.AltModifier:
            self.navigate_back()
            
        # Alt+Right - Forward
        elif event.key() == Qt.Key_Right and event.modifiers() == Qt.AltModifier:
            self.navigate_forward()

def main():
    """Main entry point"""
    app = QApplication(sys.argv)
    app.setApplicationName("Quantum Browser")
    
    # Create and show browser window
    browser = QuantumBrowser()
    browser.show()
    
    # Start event loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
