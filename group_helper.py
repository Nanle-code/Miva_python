import streamlit as st
import webbrowser
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Group Creation Helper",
    page_icon="👥",
    layout="wide"
)

# Title and description
st.title("👥 Group Creation Platform Helper")
st.markdown("---")

# Instructions section
st.header("📋 Task Instructions")
st.info("""
This app helps you complete the group creation task:
1. Create a group
2. Add group members
3. Submit the group work when completed
""")

st.markdown("---")

# Group planning section
st.header("📝 Group Planning Workspace")

# Initialize session state
if 'group_name' not in st.session_state:
    st.session_state.group_name = ""
if 'members' not in st.session_state:
    st.session_state.members = []
if 'notes' not in st.session_state:
    st.session_state.notes = ""

# Group name input
st.subheader("1. Plan Your Group")
group_name = st.text_input(
    "Group Name",
    value=st.session_state.group_name,
    placeholder="Enter your group name"
)
st.session_state.group_name = group_name

# Member management
st.subheader("2. Add Group Members")

col1, col2 = st.columns([3, 1])
with col1:
    new_member = st.text_input(
        "Member Name/Email",
        placeholder="Enter member name or email",
        key="new_member_input"
    )
with col2:
    st.write("")  # Spacing
    st.write("")  # Spacing
    if st.button("➕ Add Member"):
        if new_member and new_member.strip():
            st.session_state.members.append({
                "name": new_member.strip(),
                "added_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            st.rerun()

# Display members
if st.session_state.members:
    st.write("**Current Members:**")
    for idx, member in enumerate(st.session_state.members):
        col1, col2, col3 = st.columns([0.5, 3, 0.5])
        with col1:
            st.write(f"{idx + 1}.")
        with col2:
            st.write(f"**{member['name']}** _(added: {member['added_at']})_")
        with col3:
            if st.button("🗑️", key=f"delete_{idx}"):
                st.session_state.members.pop(idx)
                st.rerun()
else:
    st.info("No members added yet. Add members using the form above.")

# Notes section
st.subheader("3. Work Notes & Progress")
notes = st.text_area(
    "Notes",
    value=st.session_state.notes,
    placeholder="Track your progress, tasks, or any important information here...",
    height=150
)
st.session_state.notes = notes

# Summary section
st.markdown("---")
st.header("📊 Summary")

summary_col1, summary_col2, summary_col3 = st.columns(3)
with summary_col1:
    st.metric("Group Name", st.session_state.group_name if st.session_state.group_name else "Not set")
with summary_col2:
    st.metric("Total Members", len(st.session_state.members))
with summary_col3:
    completion = "✅ Ready" if st.session_state.group_name and st.session_state.members else "⚠️ Incomplete"
    st.metric("Status", completion)

# Checklist
st.subheader("✅ Completion Checklist")
col1, col2 = st.columns(2)

with col1:
    st.checkbox("Group created on platform", key="check_1")
    st.checkbox("All members added", key="check_2")
with col2:
    st.checkbox("Work completed", key="check_3")
    st.checkbox("Submission completed", key="check_4")

# Final action buttons
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔄 Clear All Data", type="secondary"):
        st.session_state.group_name = ""
        st.session_state.members = []
        st.session_state.notes = ""
        st.rerun()

with col2:
    if st.button("💾 Export Summary"):
        summary_text = f"""
GROUP CREATION SUMMARY
=====================
Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

Group Name: {st.session_state.group_name}

Members ({len(st.session_state.members)}):
{chr(10).join([f"  - {m['name']}" for m in st.session_state.members])}

Notes:
{st.session_state.notes}
"""
        st.download_button(
            label="📥 Download Summary",
            data=summary_text,
            file_name=f"group_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain"
        )

# Footer
st.markdown("---")
st.caption("💡 Tip: Use this app to plan and track your group creation progress before submitting on the platform.")