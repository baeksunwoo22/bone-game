import streamlit as st
import random
import time

# 1. Page Configuration
st.set_page_config(page_title="Human Anatomy Pro", page_icon="💀", layout="centered")

# 2. Medical Data (35 Bones with English Terms)
bone_data = {
    "Skull (Cranium)": {"pos": (8, 50), "options": ["Skull", "Mandible", "Cervical", "Clavicle"]},
    "Mandible": {"pos": (14, 50), "options": ["Mandible", "Maxilla", "Hyoid", "Skull"]},
    "Maxilla": {"pos": (11, 50), "options": ["Maxilla", "Zygomatic", "Nasal", "Mandible"]},
    "Cervical Vertebrae": {"pos": (18, 50), "options": ["Cervical", "Thoracic", "Lumbar", "Sacrum"]},
    "Clavicle": {"pos": (22, 40), "options": ["Clavicle", "Scapula", "Sternum", "Humerus"]},
    "Scapula": {"pos": (25, 35), "options": ["Scapula", "Clavicle", "Humerus", "Ribs"]},
    "Sternum": {"pos": (32, 50), "options": ["Sternum", "Xiphoid", "Ribs", "Clavicle"]},
    "Ribs": {"pos": (38, 42), "options": ["Ribs", "Sternum", "Spine", "Pelvis"]},
    "Humerus": {"pos": (40, 30), "options": ["Humerus", "Radius", "Ulna", "Femur"]},
    "Radius": {"pos": (52, 25), "options": ["Radius", "Ulna", "Carpals", "Humerus"]},
    "Ulna": {"pos": (52, 28), "options": ["Ulna", "Radius", "Metacarpals", "Humerus"]},
    "Carpals": {"pos": (58, 22), "options": ["Carpals", "Metacarpals", "Phalanges", "Tarsals"]},
    "Metacarpals": {"pos": (61, 20), "options": ["Metacarpals", "Carpals", "Phalanges", "Radius"]},
    "Phalanges (Hand)": {"pos": (65, 18), "options": ["Phalanges", "Metacarpals", "Carpals", "Ulna"]},
    "Thoracic Vertebrae": {"pos": (38, 50), "options": ["Thoracic", "Cervical", "Lumbar", "Sacrum"]},
    "Lumbar Vertebrae": {"pos": (50, 50), "options": ["Lumbar", "Thoracic", "Sacrum", "Coccyx"]},
    "Pelvis (Ilium)": {"pos": (58, 45), "options": ["Pelvis", "Sacrum", "Femur", "Ischium"]},
    "Sacrum": {"pos": (63, 50), "options": ["Sacrum", "Coccyx", "Lumbar", "Pelvis"]},
    "Coccyx": {"pos": (66, 50), "options": ["Coccyx", "Sacrum", "Pelvis", "Femur"]},
    "Femur": {"pos": (75, 42), "options": ["Femur", "Tibia", "Fibula", "Patella"]},
    "Patella": {"pos": (82, 42), "options": ["Patella", "Femur", "Tibia", "Fibula"]},
    "Tibia": {"pos": (90, 40), "options": ["Tibia", "Fibula", "Femur", "Tarsals"]},
    "Fibula": {"pos": (90, 44), "options": ["Fibula", "Tibia", "Patella", "Talus"]},
    "Tarsals": {"pos": (95, 42), "options": ["Tarsals", "Metatarsals", "Phalanges", "Calcaneus"]},
    "Metatarsals": {"pos": (97, 44), "options": ["Metatarsals", "Tarsals", "Phalanges", "Tibia"]},
    "Phalanges (Foot)": {"pos": (98, 47), "options": ["Phalanges", "Metatarsals", "Tarsals", "Fibula"]},
    "Calcaneus": {"pos": (96, 40), "options": ["Calcaneus", "Talus", "Tarsals", "Tibia"]},
    "Talus": {"pos": (93, 43), "options": ["Talus", "Calcaneus", "Tibia", "Fibula"]},
    "Ischium": {"pos": (62, 47), "options": ["Ischium", "Ilium", "Pubis", "Sacrum"]},
    "Pubis": {"pos": (62, 50), "options": ["Pubis", "Ischium", "Ilium", "Coccyx"]},
    "Femoral Head": {"pos": (67, 45), "options": ["Femoral Head", "Femur", "Pelvis", "Sacrum"]},
    "Zygomatic Bone": {"pos": (12, 45), "options": ["Zygomatic", "Nasal", "Maxilla", "Skull"]},
    "Nasal Bone": {"pos": (10, 48), "options": ["Nasal", "Maxilla", "Zygomatic", "Skull"]},
    "Acromion": {"pos": (24, 34), "options": ["Acromion", "Coracoid", "Scapula", "Clavicle"]},
    "Xiphoid Process": {"pos": (35, 50), "options": ["Xiphoid", "Sternum", "Ribs", "Lumbar"]}
}

# Session State Initialization
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_bone' not in st.session_state:
    st.session_state.current_bone = random.choice(list(bone_data.keys()))
if 'quiz_count' not in st.session_state:
    st.session_state.quiz_count = 0

st.title("💀 AI Remote Anatomy Diagnostic System")
st.write("Identify the bone highlighted by the red marker. (Professional English Version)")

# 3. Visual Interface
top, left = bone_data[st.session_state.current_bone]["pos"]

st.markdown(f"""
    <div style="background-color: #1e2a38; height: 550px; position: relative; border-radius: 20px; border: 2px solid #4a90e2; display: flex; justify-content: center; overflow: hidden;">
        <!-- Anatomy Silhouette (Medical Blue Style) -->
        <div style="width: 180px; height: 500px; background: linear-gradient(180deg, #2c3e50 0%, #34495e 100%); border-radius: 90px 90px 40px 40px; margin-top: 25px; position: relative; opacity: 0.8; border: 1px solid #5d6d7e;">
            <!-- Head -->
            <div style="width: 70px; height: 85px; background-color: #2c3e50; border-radius: 50%; position: absolute; top: -20px; left: 55px; border: 1px solid #5d6d7e;"></div>
            <!-- Target Dot -->
            <div style="position: absolute; top: {top}%; left: {left}%; width: 18px; height: 18px; background-color: #ff4757; border-radius: 50%; border: 2px solid #ffffff; box-shadow: 0 0 20px #ff4757; z-index: 100; transform: translate(-50%, -50%);"></div>
        </div>
        <div style="position: absolute; bottom: 10px; right: 20px; color: #4a90e2; font-size: 0.8rem;">ANATOMICAL DATA v2.5</div>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# 4. Quiz Section
options = bone_data[st.session_state.current_bone]["options"]
random.shuffle(options)

st.subheader("❓ What is the medical term for this bone?")
cols = st.columns(2)
for i, option in enumerate(options):
    with cols[i % 2]:
        if st.button(option, key=f"{option}_{st.session_state.quiz_count}", use_container_width=True):
            if option == st.session_state.current_bone:
                st.success(f"🎯 CORRECT: {st.session_state.current_bone}")
                st.session_state.score += 10
                st.session_state.quiz_count += 1
                st.session_state.current_bone = random.choice(list(bone_data.keys()))
                time.sleep(0.7)
                st.rerun()
            else:
                st.error("❌ INCORRECT. Review the anatomical position.")

# 5. Professional Dashboard
st.sidebar.header("📊 Clinical Metrics")
st.sidebar.metric("Total Score", f"{st.session_state.score}")
st.sidebar.metric("Solved Cases", f"{st.session_state.quiz_count}")

if st.sidebar.button("Reset Session"):
    st.session_state.score = 0
    st.session_state.quiz_count = 0
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.write("**Digital Healthcare Concept:**")
st.sidebar.caption("Ensuring accurate communication between patients and clinicians through anatomical literacy.")
