import streamlit as st

def main():
    st.set_page_config(
        page_title="High Five - Camera An Toàn Cho Trẻ",
        page_icon="👶",
        layout="wide"
    )

    # Tiêu đề chính
    st.title("🛡️ High Five - Giải Pháp An Toàn Cho Trẻ")
    
    # Phần giới thiệu về nhóm
    st.header("Về Chúng Tôi")
    st.write("""
    High Five với sứ mệnh bảo vệ trẻ em khỏi các nguy cơ bạo hành và xâm hại. 
    Chúng tôi tin rằng mọi đứa trẻ đều xứng đáng được sống trong môi trường an toàn và được yêu thương.
    """)

    # Phần sản phẩm
    st.header("🎥 Camera Chống Bạo Hành Trẻ Em")
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("team.jpg", caption="Mô hình camera High Five")
        st.write("""
        **Tính Năng Nổi Bật:**
        - Nhận diện hành vi bạo hành với độ chính xác cao
        - Cảnh báo ngay lập tức qua điện thoại
        - Ghi hình chất lượng cao
        - Kết nối dễ dàng với ứng dụng di động
        """)

    with col2:
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # Video demo (placeholder)

    # Phần video giới thiệu
    st.header("🎞️ Các Video Liên Quan")
    
    video_sources = [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "https://www.youtube.com/watch?v=3JZ_D3ELwUQ",
        "https://www.youtube.com/watch?v=6n3pFFPSlAk"
    ]
    
    cols = st.columns(3)
    for i, video in enumerate(video_sources):
        with cols[i]:
            st.video(video)
    st.markdown("© 2024 High Five - Vì Sự An Toàn Của Trẻ Em")

if __name__ == "__main__":
    main()