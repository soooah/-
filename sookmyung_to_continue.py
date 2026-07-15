import streamlit as st

###################
# 페이지 기본 설정 #
###################
st.set_page_config(
    page_title="이어질 숙명",
    layout="wide"
)

###########################
# 현재 선택된 대화 상대 저장 #
###########################
if "selected_user" not in st.session_state:
    st.session_state.selected_user = "김민지 멘티"

#####################
# 사용자별 채팅 내용 #
#####################
if "chat_data" not in st.session_state:

    st.session_state.chat_data = {

        "김민지 멘티": [
            {"role": "assistant", "content": "🎉 매칭에 성공했어요!"},
            {"role": "assistant", "content": "안녕하세요! 만나서 반가워요 😊"}
        ],

        "박지훈 멘토": [
            {"role": "assistant", "content": "🎉 매칭에 성공했어요!"},
            {"role": "assistant", "content": "멘토링 신청 감사합니다!"},
            {"role": "assistant", "content": "궁금한 점 있으면 편하게 질문하세요."}
        ],

        "이서연 멘티": [
            {"role": "assistant", "content": "🎉 매칭에 성공했어요!"},
            {"role": "assistant", "content": "같이 공부해요! 📚"}
        ]
    }

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

    # 현재 선택한 사람 표시
    st.subheader(f"👤 {st.session_state.selected_user}")

    # 현재 사람의 채팅 가져오기
    messages = st.session_state.chat_data[
        st.session_state.selected_user
    ]

    # 채팅 출력
    for message in messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # 채팅 입력창
    user_input = st.chat_input("메시지를 입력하세요.")

    # 메시지를 보내면 현재 채팅방에 저장
    if user_input:

        st.session_state.chat_data[
            st.session_state.selected_user
        ].append(
            {
                "role": "user",
                "content": user_input
            }
        )

        st.rerun()

############
# 하단 메뉴 #
############
st.divider()

bottom1, bottom2 = st.columns([2, 8])

with bottom1:
    st.button("🏠 메인으로")

with bottom2:
    st.empty()
