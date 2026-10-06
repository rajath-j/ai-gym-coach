import os
import streamlit as st
import streamlit.components.v1 as components
import base64
 
# load_css -> Function to load a CSS file and inject it into the Streamlit app.
def load_css(file_path):
    if os.path.exists(file_path):
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# inject_local_font -> Function to inject a local font into the Streamlit app.
def inject_local_font(font_path, font_name):
    if not os.path.exists(font_path):
        return
    
    with open(font_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    #ext -> extension of the font file without the leading dot
    ext = os.path.splitext(font_path)[1].lstrip(".")
    # fmt -> format of the font file for CSS, default to the extension if not found in the mapping
    fmt = {"otf": "opentype"}.get(ext, ext)
    # mime -> MIME type of the font file for CSS, default to "font/{ext}" if not found in the mapping
    mime = {"otf": "font/otf"}.get(ext, f"font/{ext}")
    # Inject the font into the Streamlit app using a <style> tag with @font-face rule 
    st.markdown(f"""
        <style>
        @font-face {{
            font-family: '{font_name}';
            src: url('data:{mime};base64,{encoded}') format('{fmt}');
            font-weight: 100 900;
            font-style: normal;
        }}
        </style>
    """, unsafe_allow_html=True)

def inject_webrtc_styles():
    font_path = os.path.join(os.getcwd(), "static", "AdobeClean.otf")
    
    if not os.path.exists(font_path):
        return

    with open(font_path, "rb") as font_file:
        encoded_font = base64.b64encode(font_file.read()).decode()
    # Inject custom styles into the WebRTC iframe using JavaScript for Streamlit 
    # The script finds the WebRTC iframe and injects a <style> tag with @font-face rule and custom styles for buttons.
    
    components.html(
        f"""
        <script>
        (function patchWebRTCStyles() {{
            function injectIntoIframe(iframe) {{
                try {{
                    const doc = iframe.contentDocument || iframe.contentWindow.document;
                    if (!doc || !doc.head) return;
                    if (doc.head.querySelector('#webrtc-custom-styles')) return;
                    const style = doc.createElement('style');
                    style.id = 'webrtc-custom-styles';
                    style.textContent = `
                        @font-face {{
                            font-family: 'AdobeClean';
                            src: url('data:font/otf;base64,{encoded_font}') format('opentype');
                            font-weight: 100 900;
                            font-style: normal;
                        }}
                        .MuiButtonBase-root,
                        .MuiButton-root,
                        .MuiButton-contained,
                        .MuiButton-text {{
                            border-radius: 0 !important;
                            font-family: 'AdobeClean', sans-serif !important;
                            letter-spacing: 0.05em !important;
                        }}
                    `;
                    doc.head.appendChild(style);
                }} catch (e) {{
                    console.warn('[patcher] could not inject:', e);
                }}
            }}

            function findAndPatch() {{
                const parentDoc = window.parent.document;
                const iframes = parentDoc.querySelectorAll('iframe');
                iframes.forEach(iframe => {{
                    if (iframe.src && iframe.src.includes('webrtc')) {{
                        if (iframe.contentDocument && iframe.contentDocument.readyState === 'complete') {{
                            injectIntoIframe(iframe);
                        }} else {{
                            iframe.addEventListener('load', () => injectIntoIframe(iframe));
                        }}
                    }}
                }});
            }}

            findAndPatch();
        }})();
        </script>
        """,
        height=0,
    )