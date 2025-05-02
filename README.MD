# Intelium: Universal Automation Framework

[![Intelium Preview](https://img.youtube.com/vi/OoZpDdprG1o/0.jpg)](https://youtu.be/OoZpDdprG1o)

## 🚀 Vision

Intelium is not just another automation framework - it's a vision for a world where any digital interaction can be automated with human-like precision. Whether you're automating browser interactions, desktop applications, or complex workflows, Intelium provides a unified, intelligent approach to automation that feels natural and reliable.

## ✨ Key Features

### 🤖 Human-Like Interactions
- Natural mouse movements with randomized offsets
- Variable typing speeds with realistic timing
- Smooth scrolling with acceleration/deceleration
- Intelligent element detection with tolerance for visual variations

### 🌐 Universal Automation
- **Browser Automation**: Support for Selenium, Playwright, and more
- **Desktop Automation**: Native system interactions with OCR capabilities
- **Cross-Platform**: Works seamlessly across Windows, macOS, and Linux
- **Extensible**: Easy to add support for new automation targets

### 🎯 Smart Element Detection
- Template matching with scale and rotation tolerance
- OCR-powered text detection (optional)
- Confidence-based matching
- Duplicate detection and filtering

### ⚡ Performance & Reliability
- Asynchronous operation support
- Robust error handling
- Viewport-aware interactions
- Resource-efficient operation

## 🛠️ Quick Start

```python
from intelium import DesktopAutomation, BrowserAutomation

# Desktop Automation
desktop = DesktopAutomation()
desktop.move_to({'x': 100, 'y': 100})
desktop.click_at({'x': 100, 'y': 100})

# Browser Automation
from selenium import webdriver
driver = webdriver.Chrome()
browser = BrowserAutomation(driver)
element = driver.find_element("id", "my-button")
browser.click_at(element)
```

## 🔧 Installation

```bash
pip install intelium
```

## 📚 Usage Examples

### Desktop Automation
```python
from intelium import DesktopAutomation

# Initialize with OCR support
automation = DesktopAutomation(ocr=True)

# Find elements by image
elements = automation.find_elements(
    image_path="button.png",
    min_confidence=0.8
)

# Find elements by text
text_elements = automation.find_text_elements(
    query="Click me",
    min_confidence=0.8
)

# Interact with elements
for element in elements:
    automation.move_to(element)
    automation.click_at(element)
    automation.type_at(element, "Hello, World!")
```

### Browser Automation
```python
from intelium import BrowserAutomation
from selenium import webdriver

driver = webdriver.Chrome()
automation = BrowserAutomation(driver)

# Navigate and interact
driver.get("https://example.com")
element = driver.find_element("id", "search")
automation.type_at(element, "Search query")
automation.click_at(element)
```

## 🎯 Use Cases

### 🤖 RPA (Robotic Process Automation)
- Automate repetitive desktop tasks
- Fill forms and process documents
- Extract data from various sources
- Integrate with existing workflows

### 🧪 Testing & QA
- Automated UI testing
- Cross-browser testing
- Visual regression testing
- Performance testing

### 📊 Data Collection
- Web scraping with human-like behavior
- Automated data entry
- Document processing
- Data extraction from various sources

### 🔄 Workflow Automation
- Business process automation
- Task scheduling and execution
- System integration
- Automated reporting

## 🔮 Future Vision

Intelium is constantly evolving to support:
- AI-powered element detection
- Natural language automation commands
- Cross-device automation
- Cloud-based automation orchestration
- Advanced pattern recognition
- Machine learning for interaction optimization

## 🤝 Contributing

We welcome contributions! Whether it's:
- Bug reports
- Feature requests
- Code contributions
- Documentation improvements
- Testing and feedback

## 📄 License

This project is dual-licensed under:
1. MIT License - for general use and distribution
2. Intelium Attribution License - requiring proper attribution

The MIT License allows you to use, modify, and distribute the software freely, while the Intelium Attribution License ensures proper credit is given to the original authors. See the [LICENSE](LICENSE) file for full details.

When using Intelium, you must include the following attribution in your project:
```
This project uses Intelium (https://github.com/Leadrive/intelium), 
developed by Ali Shahmir Khan, based on the original work by Vladislav Zenkevich.
```

---

Made with ❤️ by Ali Shahmir Khan
Original Author: Vladislav Zenkevich
