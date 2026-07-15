import streamlit as st

###################
# 페이지 기본 설정 #
###################
st.set_page_config(
    page_title="이어질 숙명",
    layout="wide"
)

############
# 상단 제목 #
############
col1, col2 = st.columns([9, 1])

with col1:
    st.title("이어질 숙명")

with col2:
    st.button("🔔")

############
# 화면 분할 #
############
left, middle, right = st.columns([3, 3, 5])

###############
# 1. 채팅 목록 #
###############

with left:

    st.subheader("💬 나의 채팅 목록")

    if st.button("👤 김민지 멘티"):
    st.session_state.selected_user = "김민지 멘티"

st.caption("친해져요! 😊")

if st.button("👤 박지훈 멘토"):
    st.session_state.selected_user = "박지훈 멘토"

st.caption("학교생활이 궁금하면 편하게 물어보세요!")

if st.button("👤 이서연 멘티"):
    st.session_state.selected_user = "이서연 멘티"

st.caption("같이 공부해요!")

    st.button("➕ 새로운 매칭 시작하기")

################
# 2. AI 추천봇 #
################

with middle:

    st.subheader("💡 이런 주제는 어때요?")

    st.button("학교에서 가장 좋아하는 수업은?")
    st.button("MT와 축제 중 하나만 간다면?")
    st.button("방학 때 가장 하고 싶은 것은?")
    st.button("과제 VS 시험")

    st.divider()

    st.caption("원하는 메시지를 누르면 대화 상대에게 전송됩니다.")

#############
# 3. 대화창 #
#############

with right:

    st.subheader(f"👤 {st.session_state.selected_user}")

    st.info("🎉 매칭에 성공했어요!\n\n대화를 시작해볼까요?")

    st.chat_message("assistant").write("안녕하세요! 😊")

    st.chat_message("user").write("안녕하세요! 만나서 반가워요!")

    st.chat_input("메시지를 입력하세요.")

############
# 하단 메뉴 #
############

st.divider()

bottom1, bottom2 = st.columns([2, 8])

with bottom1:
    st.button("🏠 메인으로")

with bottom2:
    st.empty()
