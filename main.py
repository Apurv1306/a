import threading
import time
import webbrowser
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

# Import your Flask app as a module!
import python_app  # Rename if your backend is differently named

class WebViewApp(App):
    def build(self):
        layout = BoxLayout()
        # Wait for Flask to be ready
        threading.Thread(target=self.open_webview, daemon=True).start()
        return layout

    def open_webview(self):
        # Wait for Flask server to be ready
        for _ in range(30):
            try:
                import requests
                r = requests.get("http://127.0.0.1:5000")
                if r.ok:
                    break
            except Exception:
                time.sleep(1)
        # Open local web browser, or on mobile use a WebView widget (see KivyMD examples)
        webbrowser.open("http://127.0.0.1:5000")

def run_flask():
    python_app.app.run(host="127.0.0.1", port=5000)

if __name__ == "__main__":
    threading.Thread(target=run_flask, daemon=True).start()
    WebViewApp().run()
