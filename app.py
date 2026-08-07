import streamlit as st

st.set_page_config(
    page_title="AI Image Generation Studio",
    layout="wide",
)

st.title("AI Image Generation Studio")

st.markdown(
    """
Turn your ideas into stunning AI-generated artwork using natural language prompts.
Customize the generation settings and create high-quality images in seconds.
"""
)

left_col, right_col = st.columns([1, 1])

with left_col:

    st.header("Generation Settings")

    prompt = st.text_area(
        "Image Prompt",
        placeholder="Describe the image you would like to generate...",
        height=180,
    )

    with st.expander("Example Prompts"):

        st.write("• A futuristic city floating above the clouds at sunset")

        st.write("• A magical forest with glowing mushrooms")

        st.write("• A cyberpunk cat wearing neon glasses")

        st.write("• A medieval castle surrounded by dragons")

        st.write("• An astronaut surfing on Saturn's rings")

    style = st.selectbox(
        "Art Style",
        [
            "Realistic",
            "Digital Art",
            "Fantasy",
            "Anime",
            "Oil Painting",
            "Watercolor",
            "Sketch",
            "Cyberpunk",
            "Minimalist",
        ],
    )

    resolution = st.selectbox(
        "Image Resolution",
        [
            "512x512",
            "768x768",
            "1024x1024",
        ],
        help="Higher resolutions produce more detailed images but may take longer to generate.",
    )

    image_count = st.selectbox(
        "Number of Images",
        [1, 2, 3, 4],
        help="Choose how many image variations to generate.",
    )

    st.markdown("---")

    generate = st.button(
        "Generate Images",
        use_container_width=True,
    )

with right_col:

    st.header("Generated Images")

    st.info(
        "Your generated image(s) will appear here after clicking **Generate Images**."
    )