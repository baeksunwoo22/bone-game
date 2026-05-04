import streamlit as st
import pandas as pd

# 1. 페이지 설정 및 제목
st.set_page_config(page_title="Bone-Assemble", page_icon="🦴", layout="wide")

st.title("🦴 Bone-Assemble: 원격 재활 해부학 게임")
st.markdown("""
    **원격의료 활용 컨셉:** 환자가 자신의 골격 구조를 이해하고, 
    원격 진료 시 의사에게 통증 부위를 정확히 설명할 수 있도록 돕는 디지털 치료제(DTx) 프로토타입입니다.
""")

# 2. 게임 데이터 설정 (뼈 명칭과 올바른 위치)
bones = {
    "두개골 (Skull)": "상단 (머리)",
    "흉골 (Sternum)": "중앙 (가슴)",
    "대퇴골 (Femur)": "하단 (허벅지)",
    "척추 (Spine)": "중앙 (등)",
    "골반 (Pelvis)": "하단 (골반)"
}

# 세션 상태 초기화
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'matched' not in st.session_state:
    st.session_state.matched = []

# 3. 화면 레이아웃 분할
col1, col2 = st.columns([1.5, 1])

with col1:
    st.subheader("📍 해부학 매칭 테스트")
    
    # 아직 맞추지 못한 뼈들만 선택지에 표시
    remaining_bones = [b for b in bones.keys() if b not in st.session_state.matched]
    
    if remaining_bones:
        selected_bone = st.selectbox("맞출 뼈를 선택하세요:", remaining_bones)
        target_pos = st.radio("이 뼈의 올바른 위치는 어디일까요?", 
                              ["상단 (머리)", "중앙 (가슴)", "중앙 (등)", "하단 (골반)", "하단 (허벅지)"])

        if st.button("부위 맞추기 🎯"):
            if bones[selected_bone] == target_pos:
                st.session_state.score += 20
                st.session_state.matched.append(selected_bone)
                st.success(f"정답! {selected_bone}이(가) 제자리에 고정되었습니다.")
                st.rerun() # 화면 갱신
            else:
                st.error("위치가 틀렸습니다. 다시 한번 생각해보세요!")
    else:
        st.balloons()
        st.success("🎉 축하합니다! 모든 골격 구조를 완성했습니다.")
        if st.button("다시 시작하기"):
            st.session_state.score = 0
            st.session_state.matched = []
            st.rerun()

with col2:
    st.subheader("📊 환자 교육 리포트")
    st.metric("학습 진행률", f"{(len(st.session_state.matched) / len(bones)) * 100:.0f}%")
    st.progress(len(st.session_state.matched) / len(bones))
    
    st.write("**현재까지 파악한 부위:**")
    if st.session_state.matched:
        for b in st.session_state.matched:
            st.write(f"✅ {b}")
    else:
        st.write("아직 맞춘 부위가 없습니다.")

# 4. 하단 설명 (교수님 어필용)
st.markdown("---")
st.info("""
**💡 발표 포인트 (차별화 전략)**
1. **정밀 소통:** 환자가 '다리가 아파요' 대신 '대퇴골 부위가 아파요'라고 말할 수 있게 교육합니다.
2. **인지 재활:** 수술 후 환자의 인지 능력을 게임 데이터로 수집하여 원격으로 모니터링합니다.
""")
