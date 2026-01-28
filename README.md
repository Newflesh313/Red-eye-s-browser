# Red eye's browser - Standalone Desktop Application

A **fully self-contained desktop web browser** built from scratch using Python, PyQt5, and the Chromium rendering engine. This is a real, native Windows application with its own window - no other browsers required!

⌨️ **Keyboard Shortcuts**
- `Ctrl+T` - New Tab
- `Ctrl+W` - Close Tab
- `Ctrl+L` - Focus Address Bar
- `Ctrl+R` / `F5` - Reload
- `Alt+←` - Back
- `Alt+→` - Forward

## Installation

### Prerequisites
- **Python 3.7+** installed on your system
- **Internet connection** for downloading dependencies

### Step 1: Install Dependencies

Double-click: **`install-dependencies.bat`**

This will install:
- PyQt5 (GUI framework)
- PyQtWebEngine (Chromium browser engine)

The installation takes about 2-5 minutes.

### Step 2: Run the Browser

Double-click: **`run-browser.bat`**

The Quantum Browser will launch in its own window!

## Manual Installation (Alternative)

If the batch files don't work, run these commands manually:

```bash
pip install PyQt5 PyQtWebEngine
python quantum_browser.py
```

## How It Works

This is a **real, native desktop application**, not a web page:

1. **Python** - Programming language
2. **PyQt5** - Creates the native Windows window and UI
3. **QtWebEngine** - Embeds the Chromium browser engine
4. **Chromium** - The same rendering engine used by Google Chrome

The result is a standalone browser that works exactly like Chrome, Firefox, or Edge!

## What Makes This Different

### vs Web-Based Browser (HTML/CSS/JS)
- Runs as a native desktop application
- ✅ Has its own window with title bar
- ✅ Doesn't open in another browser
- ✅ Full Chromium rendering engine

### vs Terminal Browser  
Full graphical interface
 Renders images, videos, CSS, JavaScript
Interactive web pages work perfectly
 Looks and feels like Chrome/Edge

### vs Chrome/Firefox/Edge
Similar rendering quality (uses Chromium)
Lighter weight and customizable
 Built from scratch by you
Can be modified and extended

## File Structure

```
web-browser/
├── quantum_browser.py           # Main browser application (~400 lines)
├── requirements.txt             # Python dependencies
├── install-dependencies.bat     # Dependency installer
├── run-browser.bat             # Browser launcher
└── README.md                   # This file
```

## Customization

Edit `quantum_browser.py` to customize:

- **Home page**: Change `"https://www.google.com"` in `navigate_home()`
- **Colors**: Modify the `dark_stylesheet` in `setup_theme()`
- **Window size**: Adjust `setGeometry(100, 100, 1200, 800)`
- **Add features**: Download manager, ad blocker, extensions, etc.

## Advanced: Create Executable (.exe)

To create a standalone `.exe` file that doesn't require Python:

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Build the executable:
   ```bash
   pyinstaller --onefile --windowed --name "QuantumBrowser" quantum_browser.py
   ```

3. Find your executable in the `dist/` folder!

This creates a single `.exe` file you can run on any Windows computer without installing Python.

## Troubleshooting

### "Python is not installed"
- Download Python from https://www.python.org/downloads/
- During installation, check "Add Python to PATH"
- Restart your computer after installation

### "Failed to install dependencies"
- Make sure you have an internet connection
- Try running as administrator
- Manually run: `pip install PyQt5 PyQtWebEngine`

### Browser won't start
- Make sure dependencies are installed
- Check Python version: `python --version` (needs 3.7+)
- Try running manually: `python quantum_browser.py`

### Missing DLLs on older Windows
- Install Visual C++ Redistributable from Microsoft

## System Requirements

- **OS**: Windows 7 or later (Windows 10/11 recommended)
- **Python**: 3.7 or higher
- **RAM**: 2GB minimum (4GB+ recommended)
- **Disk**: 500MB for dependencies

## Technical Details

### Architecture:
- **GUI Framework**: PyQt5
- **Web Engine**: QtWebEngine (Chromium-based)
- **Language**: Python 3
- **Dependencies**: PyQt5, PyQtWebEngine

### Features Implemented:
 Multi-tab browsing with tab management
   URL navigation with smart search
   History tracking
   Bookmark management
   Download handling
   Keyboard shortcuts
   Dark theme UI
   Settings panel
  Status bar with progress
   Full Chromium rendering

### NOT Implemented (but can be added):
- Browser extensions
- Sync across devices
- Ad blocker
- Private browsing mode
- Password manager
- Developer tools panel

All of these can be added by extending the Python code!

## Tips

1. **First run takes longer** - Chromium engine needs to initialize
2. **Websites work exactly like Chrome** - Same rendering engine
3. **Customize freely** - The code is yours to modify
4. **Share as .exe** - Use PyInstaller to create portable executable
5. **Low resource usage** - Lighter than running full Chrome

---



