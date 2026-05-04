import streamlit as st
import random
import time

# 1. 페이지 설정
st.set_page_config(page_title="Anatomy Quiz Pro 35", page_icon="🦴", layout="centered")

# 2. 뼈 데이터 확대 (35개 주요 및 세부 부위)
bone_data = {
    # 머리 및 목 (5개)
    "두개골 (Skull)": {"pos": (8, 50), "options": ["두개골", "하악골", "경추", "관골"]},
    "하악골 (Mandible)": {"pos": (14, 50), "options": ["하악골", "두개골", "설골", "상악골"]},
    "상악골 (Maxilla)": {"pos": (11, 50), "options": ["상악골", "하악골", "비골", "관골"]},
    "경추 (Cervical Spine)": {"pos": (18, 50), "options": ["경추", "요추", "흉추", "미추"]},
    "설골 (Hyoid)": {"pos": (16, 50), "options": ["설골", "하악골", "갑상연골", "경추"]},
    
    # 상체 및 팔 (12개)
    "쇄골 (Clavicle)": {"pos": (22, 42), "options": ["쇄골", "견갑골", "흉골", "늑골"]},
    "견갑골 (Scapula)": {"pos": (25, 38), "options": ["견갑골", "쇄골", "상완골", "척추"]},
    "흉골 (Sternum)": {"pos": (30, 50), "options": ["흉골", "늑골", "쇄골", "상완골"]},
    "늑골 (Ribs)": {"pos": (35, 43), "options": ["늑골", "흉골", "요추", "골반"]},
    "상완골 (Humerus)": {"pos": (38, 32), "options": ["상완골", "요골", "척골", "대퇴골"]},
    "요골 (Radius)": {"pos": (48, 27), "options": ["요골", "척골", "상완골", "수근골"]},
    "척골 (Ulna)": {"pos": (48, 30), "options": ["척골", "요골", "중수골", "지골"]},
    "수근골 (Carpals)": {"pos": (55, 24), "options": ["수근골", "중수골", "지골", "부전골"]},
    "중수골 (Metacarpals)": {"pos": (58, 22), "options": ["중수골", "수근골", "지골", "주상골"]},
    "지골 (Phalanges - Hand)": {"pos": (62, 20), "options": ["지골", "중수골", "수근골", "척골"]},
    "오구돌기 (Coracoid)": {"pos": (24, 40), "options": ["오구돌기", "견봉", "쇄골", "상완골"]},
    "견봉 (Acromion)": {"pos": (23, 35), "options": ["견봉", "오구돌기", "견갑골", "쇄골"]},

    # 척추 및 골반 (6개)
    "흉추 (Thoracic Spine)": {"pos": (35, 50), "options": ["흉추", "경추", "요추", "천골"]},
    "요추 (Lumbar Spine)": {"pos": (48, 50), "options": ["요추", "흉추", "천골", "미추"]},
    "골반 (Pelvis)": {"pos": (55, 50), "options": ["골반", "대퇴골", "천골", "장골"]},
    "천골 (Sacrum)": {"pos": (60, 50), "options": ["천골", "미추", "요추", "골반"]},
    "미추 (Coccyx)": {"pos": (63, 50), "options": ["미추", "천골", "골반", "요추"]},
    "장골 (Ilium)": {"pos": (54, 45), "options": ["장골", "좌골", "치골", "천골"]},

    # 하체 및 다리 (12개)
    "대퇴골 (Femur)": {"pos": (70, 42), "options": ["대퇴골", "경골", "비골", "슬개골"]},
    "슬개골 (Patella)": {"pos": (78, 42), "options": ["슬개골", "대퇴골", "경골", "비골"]},
    "경골 (Tibia)": {"pos": (85, 40), "options": ["경골", "비골", "대퇴골", "족근골"]},
    "비골 (Fibula)": {"pos": (85, 44), "options": ["비골", "경골", "족근골", "중족골"]},
    "족근골 (Tarsals)": {"pos": (92, 42), "options": ["족근골", "중족골", "지골", "종골"]},
    "중족골 (Metatarsals)": {"pos": (95, 42), "options": ["중족골", "족근골", "지골", "비골"]},
    "지골 (Phalanges - Foot)": {"pos": (98, 42), "options": ["지골", "중족골", "족근골", "경골"]},
    "종골 (Calcaneus)": {"pos": (94, 45), "options": ["종골", "거골", "족근골", "지골"]},
    "거골 (Talus)": {"pos": (91, 44), "options": ["거골", "종골", "주상골", "경골"]},
    "좌골 (Ischium)": {"pos": (60, 47), "options": ["좌골", "장골", "치골", "천골"]},
    "치골 (Pubis)": {"pos": (61, 50), "options": ["치골", "좌골", "장골", "미추"]},
    "대퇴골두 (Femoral Head)": {"pos": (65, 45), "options": ["대퇴골두", "대전자", "골반", "장골"]}
}

# 세션 상태 초기화
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_bone' not in st.session_state:
    st.session_state.current_bone = random.choice(list(bone_data.keys()))
if 'quiz_count' not in st.session_state:
    st.session_state.quiz_count = 0

st.title("🦴 AI 원격 해부학 진단 가이드 (Ver 2.0)")
st.write("빨간 점이 가리키는 부위의 명칭을 맞추세요. (총 35개 정밀 부위 수록)")

# 3. 화면 레이아웃 (인체 모형 시각화)
top, left = bone_data[st.session_state.current_bone]["pos"]

st.markdown(f"""
    <div style="background-color: #f8f9fa; height: 500px; position: relative; border-radius: 20px; border: 2px solid #3498db; display: flex; justify-content: center;">
        <div style="width: 160px; height: 460px; background-color: #dee2e6; border-radius: 80px 80px 30px 30px; margin-top: 20px; position: relative; border: 1px solid #ced4da;">
            <div style="width: 65px; height: 75px; background-color: #adb5bd; border-radius: 50%; position: absolute; top: -15px; left: 47px;"></div>
            <div style="position: absolute; top: {top}%; left: {left}%; width: 20px; height: 20px; background-color: #e74c3c; border-radius: 50%; border: 3px solid white; box-shadow: 0 0 15px #e74c3c; z-index: 10; transform: translate(-50%, -50%);"></div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# 4. 문제 풀이 및 인터랙션
options = bone_data[st.session_state.current_bone]["options"]
random.shuffle(options)

st.subheader("❓ 이 부위의 정확한 의학 명칭은?")
cols = st.columns(2)
for i, option in enumerate(options):
    with cols[i % 2]:
        if st.button(option, key=f"{option}_{st.session_state.quiz_count}", use_container_width=True):
            if option == st.session_state.current_bone:
                st.success(f"🎯 정답! {st.session_state.current_bone}입니다.")
                st.session_state.score += 10
                st.session_state.quiz_count += 1
                st.session_state.current_bone = random.choice(list(bone_data.keys()))
                time.sleep(0.8)
                st.rerun()
            else:
                st.error("❌ 오답입니다. 다시 확인해보세요.")

# 5. 대시보드 (사이드바)
st.sidebar.header("📊 실시간 모니터링")
st.sidebar.metric("누적 점수", f"{st.session_state.score} 점")
st.sidebar.metric("해결한 문항", f"{st.session_state.quiz_count} 개")

if st.sidebar.button("데이터 리셋"):
    st.session_state.score = 0
    st.session_state.quiz_count = 0
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.info("이 프로토타입은 35개의 핵심 골격 데이터를 기반으로 구축되었습니다.")
