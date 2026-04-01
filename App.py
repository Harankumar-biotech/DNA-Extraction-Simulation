import streamlit as st
from PIL import Image

st.set_page_config(page_title="DNA Extraction Virtual Lab", layout="centered")

st.title("🧬 DNA Extraction Virtual Lab")
st.write("Learn the step-by-step process of DNA isolation interactively!")

# Session state to track progress
if "step" not in st.session_state:
    st.session_state.step = 1

if "mistake" not in st.session_state:
    st.session_state.mistake = False

# ---------------- STEP 1 ----------------
if st.session_state.step == 1:
    st.header("Step 1: Cell Lysis")

    st.write("Break open the cells to release DNA.")

    option = st.selectbox(
        "Choose reagent:",
        ["Select", "Detergent", "Ethanol", "Water"]
    )

    if st.button("Submit"):
        if option == "Detergent":
            st.success("✅ Correct! Cell membrane dissolved.")
            st.session_state.step = 2
        else:
            st.error("❌ Wrong choice! Cells did not lyse.")
            st.session_state.mistake = True

# ---------------- STEP 2 ----------------
elif st.session_state.step == 2:
    st.header("Step 2: Remove Proteins")

    st.write("Remove proteins using enzyme.")

    option = st.selectbox(
        "Choose reagent:",
        ["Select", "Protease", "Salt", "Ethanol"]
    )

    if st.button("Submit"):
        if option == "Protease":
            st.success("✅ Proteins removed successfully!")
            st.session_state.step = 3
        else:
            st.error("❌ Proteins still present!")
            st.session_state.mistake = True

# ---------------- STEP 3 ----------------
elif st.session_state.step == 3:
    st.header("Step 3: DNA Precipitation")

    st.write("Add alcohol to precipitate DNA.")

    option = st.selectbox(
        "Choose reagent:",
        ["Select", "Ethanol", "Detergent", "Buffer"]
    )

    if st.button("Submit"):
        if option == "Ethanol":
            st.success("🎉 DNA precipitated successfully!")

            # Show DNA image
            try:
                img = Image.open("assets/dna.png")
                st.image(img, caption="DNA Strands Forming")
            except:
                st.info("DNA visualization here (add image in assets folder)")

            st.session_state.step = 4
        else:
            st.error("❌ DNA did not precipitate.")
            st.session_state.mistake = True

# ---------------- FINAL ----------------
elif st.session_state.step == 4:
    st.header("🏁 Experiment Completed")

    if st.session_state.mistake:
        st.warning("⚠️ You made some mistakes. Try again for a perfect run!")
    else:
        st.success("🌟 Perfect experiment! Well done.")

    if st.button("Restart"):
        st.session_state.step = 1
        st.session_state.mistake = False
