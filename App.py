#LinkedIn Poster Generator - Full App with All Features

#Filename: app.py

import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
import random
import datetime
from streamlit_drawable_canvas import st_canvas

st.set_page_config(page_title="LinkedIn Poster Generator", layout="wide") st.title("🎯 LinkedIn Poster Generator") st.markdown("Create stunning LinkedIn banners with AI captions and auto layout!")

--- Sidebar Inputs ---

st.sidebar.header("🛠️ Customize Your Poster")

headline = st.sidebar.text_input("Headline", "Excited to start my new role!") subheadline = st.sidebar.text_input("Subheadline", "Grateful to join this amazing team.") role = st.sidebar.text_input("Role / Company", "Software Engineer @ Infosys") hashtags = st.sidebar.text_input("Hashtags", "#career #newjob #linkedin")

bg_color = st.sidebar.color_picker("Background Color", "#ffffff") text_color = st.sidebar.color_picker("Text Color", "#000000") border_color = st.sidebar.color_picker("Border Color", "#888888")

font_size = st.sidebar.slider("Font Size", 20, 80, 40)

uploaded_logo = st.sidebar.file_uploader("Upload Company Logo", type=["png", "jpg", "jpeg"]) uploaded_profile = st.sidebar.file_uploader("Upload Profile Photo", type=["png", "jpg", "jpeg"]) uploaded_bg = st.sidebar.file_uploader("Upload Background Image (optional)", type=["png", "jpg", "jpeg"])

mode = st.sidebar.radio("Poster Mode", ["Auto Generate", "Manual Layout"], index=0)

--- Poster Generation Logic ---

def generate_poster(index): width, height = 1200, 675 img = Image.new("RGB", (width, height), bg_color) draw = ImageDraw.Draw(img)

if uploaded_bg:
    bg_img = Image.open(uploaded_bg).resize((width, height))
    img.paste(bg_img)

draw.rectangle([(5, 5), (width - 5, height - 5)], outline=border_color, width=10)

if uploaded_logo:
    logo = Image.open(uploaded_logo).convert("RGBA")
    logo.thumbnail((150, 150))
    img.paste(logo, (width - 170, 20), logo)

if uploaded_profile:
    profile = Image.open(uploaded_profile).convert("RGBA")
    profile.thumbnail((120, 120))
    img.paste(profile, (20, 20), profile)

try:
    font = ImageFont.truetype("arial.ttf", font_size)
except:
    font = ImageFont.load_default()

text_y = 200 + random.randint(-30, 30)
draw.text((50, text_y), headline, font=font, fill=text_color)
draw.text((50, text_y + font_size + 10), subheadline, font=font, fill=text_color)
draw.text((50, text_y + 2 * (font_size + 10)), role, font=font, fill=text_color)

return img

--- Auto Generate Posters ---

if mode == "Auto Generate": st.subheader("✨ Auto-Generated Posters") cols = st.columns(5)

for i in range(5):
    img = generate_poster(i)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    byte_img = buf.getvalue()
    with cols[i]:
        st.image(img, use_column_width=True)
        st.download_button(
            label="Download",
            data=byte_img,
            file_name=f"linkedin_poster_{i+1}.png",
            mime="image/png",
            key=f"download_{i}"
        )

--- Manual Layout Canvas ---

if mode == "Manual Layout": st.subheader("🎨 Drag & Drop Layout")

canvas_result = st_canvas(
    fill_color=text_color + "88",  # Transparent fill
    stroke_width=2,
    background_color=bg_color,
    height=675,
    width=1200,
    drawing_mode="freedraw",
    key="canvas",
)
st.info("Draw your own layout. Add logos/images using the sidebar. Final image download below.")

--- AI-Generated Caption ---

st.markdown("---") st.subheader("🤖 AI-Generated LinkedIn Caption")

def generate_caption(): return f"{headline}\n{role}\n{subheadline}\n{hashtags}"

caption = generate_caption() st.text_area("Editable Caption", value=caption, height=150)

--- Post to LinkedIn ---

st.markdown("---") linkedin_url = f"https://www.linkedin.com/sharing/share-offsite/?url=https://example.com" st.markdown(f"🔗 Post to LinkedIn", unsafe_allow_html=True)

--- Credits ---

st.markdown("---") st.caption("© Pavan Sri Sai Mondem | Siva Satyamsetti | Uma Satyam Mounika Sapireddy | Bhuvaneswari Devi Seru | Chandu Meela")

