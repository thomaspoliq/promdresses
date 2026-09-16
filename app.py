import streamlit as st

# -------------------------------------------------------
# Streamlit Page Configuration
# -------------------------------------------------------
st.set_page_config(
    page_title="Prom Dresses | Fashion Guide",
    page_icon="👗",
    layout="wide",
)

# -------------------------------------------------------
# Custom CSS
# -------------------------------------------------------
st.markdown("""
<style>
.main{
    padding:2rem;
}
h1,h2,h3{
    color:#C2185B;
}
.stButton>button{
    background:#C2185B;
    color:white;
    border-radius:8px;
}
.footer{
    text-align:center;
    color:gray;
    padding-top:30px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# Header
# -------------------------------------------------------
st.title("👗 Prom Dresses – Your Complete Fashion Guide")

st.markdown("""
Choosing the perfect prom dress is one of the most exciting parts of preparing for a
special event. Whether you're attending your first prom, a graduation celebration,
or another formal occasion, selecting a dress that reflects your personality and
style can make the experience even more memorable.

👉 **Official Website:** https://promdressesin.co.uk/
""")

st.image(
    "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=1200",
    use_container_width=True
)

# -------------------------------------------------------
# Introduction
# -------------------------------------------------------
st.header("Introduction")

st.write("""
Fashion is more than simply wearing beautiful clothes. It is a way of expressing
confidence, creativity, and individuality. Prom events are among the most memorable
occasions in a student's life, making it important to find an outfit that combines
comfort, elegance, and modern fashion trends.

The website **Prom Dresses** provides fashion inspiration, shopping advice,
and styling ideas for anyone looking for beautiful dresses for prom,
evening parties, formal dinners, or special celebrations.

Visit the official website:

https://promdressesin.co.uk/
""")

# -------------------------------------------------------
# Why Prom Dresses Matter
# -------------------------------------------------------
st.header("Why Choosing the Right Prom Dress Matters")

st.write("""
A well-selected prom dress helps you feel confident throughout the event.
The perfect dress should complement your personality while remaining comfortable
enough for dancing, photographs, and socializing.

When selecting a dress, consider:

• Comfort

• Fabric Quality

• Proper Fit

• Budget

• Event Theme

• Personal Style

Choosing wisely helps create lasting memories and beautiful photographs.
""")

# -------------------------------------------------------
# Popular Dress Styles
# -------------------------------------------------------
st.header("Popular Prom Dress Styles")

styles = [
    "A-Line Dresses",
    "Ball Gowns",
    "Mermaid Dresses",
    "Empire Waist Dresses",
    "Off-the-Shoulder Dresses",
    "One-Shoulder Dresses",
    "High-Low Dresses",
    "Bodycon Dresses",
    "Sheath Dresses",
    "Princess Dresses",
]

for item in styles:
    st.markdown(f"- {item}")

# -------------------------------------------------------
# Trending Colours
# -------------------------------------------------------
st.header("Trending Colours")

colors = [
    "Emerald Green",
    "Royal Blue",
    "Classic Black",
    "Burgundy",
    "Lavender",
    "Champagne Gold",
    "Silver",
    "Blush Pink",
    "Red",
    "Navy Blue",
]

st.write(
    """
Fashion trends change every year, but these colours continue to remain among
the most popular choices for prom events.
"""
)

st.write(colors)

# -------------------------------------------------------
# Best Fabrics
# -------------------------------------------------------
st.header("Best Fabrics for Prom Dresses")

st.write("""
Choosing the right fabric is equally important because it affects the appearance,
comfort, and durability of the dress.

Popular fabrics include:

• Satin

• Chiffon

• Lace

• Silk

• Velvet

• Organza

• Tulle

• Sequin Fabric
""")

# -------------------------------------------------------
# Accessories
# -------------------------------------------------------
st.header("Accessories")

st.write("""
Accessories complete your overall appearance.

Recommended accessories include:

✔ Elegant High Heels

✔ Matching Clutch Bag

✔ Diamond Earrings

✔ Necklaces

✔ Bracelets

✔ Hair Accessories

✔ Light Makeup

✔ Comfortable Shoes for Dancing
""")

# -------------------------------------------------------
# Shopping Tips
# -------------------------------------------------------
st.header("Shopping Tips")

tips = [
    "Know your body measurements.",
    "Set your budget before shopping.",
    "Compare multiple dress styles.",
    "Choose comfortable fabrics.",
    "Read customer reviews.",
    "Check the size guide carefully.",
    "Order early.",
    "Review the return policy.",
    "Select matching accessories.",
    "Don't forget alterations if necessary."
]

for i, tip in enumerate(tips, start=1):
    st.write(f"{i}. {tip}")

# -------------------------------------------------------
# Fashion Trends
# -------------------------------------------------------
st.header("Latest Fashion Trends")

st.write("""
Modern fashion trends include minimalist dresses, floral embroidery,
sequined evening gowns, elegant satin fabrics, and sustainable fashion choices.
Many people also prefer timeless colours that can be worn on multiple occasions.

Fashion continues to evolve, offering countless options for every style,
budget, and personality.
""")

# -------------------------------------------------------
# Why Visit the Website
# -------------------------------------------------------
st.header("Why Visit Prom Dresses?")

st.write("""
The website offers articles and fashion inspiration covering:

• Prom Dresses

• Evening Dresses

• Styling Tips

• Fashion Advice

• Seasonal Trends

• Beauty Inspiration

• Shopping Guides

• Accessories
""")

st.success("Official Website: https://promdressesin.co.uk/")

# -------------------------------------------------------
# Conclusion
# -------------------------------------------------------
st.header("Conclusion")

st.write("""
Finding the perfect prom dress is about more than following trends.
The ideal outfit should reflect your personality, fit comfortably,
and make you feel confident throughout your special event.

Whether you prefer timeless elegance or contemporary fashion,
researching different styles and planning ahead can help you make
an informed choice.

For additional fashion inspiration, styling advice, and informative
articles about prom dresses, visit:

https://promdressesin.co.uk/

Explore the latest fashion trends, discover elegant outfit ideas,
and find helpful guides for your next special occasion.
""")

# -------------------------------------------------------
# Footer
# -------------------------------------------------------
st.markdown("---")

st.markdown("""
<div class='footer'>
© 2026 Fashion Guide | Powered by Streamlit<br><br>
Official Website: https://promdressesin.co.uk/
</div>
""", unsafe_allow_html=True)
