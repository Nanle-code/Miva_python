# import streamlit as st
# import webbrowser
# from datetime import datetime

# # Page configuration
# st.set_page_config(
#     page_title="Group Creation Helper",
#     page_icon="👥",
#     layout="wide"
# )

# # Title and description
# st.title("👥 Group Creation Platform Helper")
# st.markdown("---")

# # Instructions section
# st.header("📋 Task Instructions")
# st.info("""
# This app helps you complete the group creation task:
# 1. Create a group
# 2. Add group members
# 3. Submit the group work when completed
# """)

# st.markdown("---")

# # Group planning section
# st.header("📝 Group Planning Workspace")

# # Initialize session state
# if 'group_name' not in st.session_state:
#     st.session_state.group_name = ""
# if 'members' not in st.session_state:
#     st.session_state.members = []
# if 'notes' not in st.session_state:
#     st.session_state.notes = ""

# # Group name input
# st.subheader("1. Plan Your Group")
# group_name = st.text_input(
#     "Group Name",
#     value=st.session_state.group_name,
#     placeholder="Enter your group name"
# )
# st.session_state.group_name = group_name

# # Member management
# st.subheader("2. Add Group Members")

# col1, col2 = st.columns([3, 1])
# with col1:
#     new_member = st.text_input(
#         "Member Name/Email",
#         placeholder="Enter member name or email",
#         key="new_member_input"
#     )
# with col2:
#     st.write("")  # Spacing
#     st.write("")  # Spacing
#     if st.button("➕ Add Member"):
#         if new_member and new_member.strip():
#             st.session_state.members.append({
#                 "name": new_member.strip(),
#                 "added_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             })
#             st.rerun()

# # Display members
# if st.session_state.members:
#     st.write("**Current Members:**")
#     for idx, member in enumerate(st.session_state.members):
#         col1, col2, col3 = st.columns([0.5, 3, 0.5])
#         with col1:
#             st.write(f"{idx + 1}.")
#         with col2:
#             st.write(f"**{member['name']}** _(added: {member['added_at']})_")
#         with col3:
#             if st.button("🗑️", key=f"delete_{idx}"):
#                 st.session_state.members.pop(idx)
#                 st.rerun()
# else:
#     st.info("No members added yet. Add members using the form above.")

# # Notes section
# st.subheader("3. Work Notes & Progress")
# notes = st.text_area(
#     "Notes",
#     value=st.session_state.notes,
#     placeholder="Track your progress, tasks, or any important information here...",
#     height=150
# )
# st.session_state.notes = notes

# # Summary section
# st.markdown("---")
# st.header("📊 Summary")

# summary_col1, summary_col2, summary_col3 = st.columns(3)
# with summary_col1:
#     st.metric("Group Name", st.session_state.group_name if st.session_state.group_name else "Not set")
# with summary_col2:
#     st.metric("Total Members", len(st.session_state.members))
# with summary_col3:
#     completion = "✅ Ready" if st.session_state.group_name and st.session_state.members else "⚠️ Incomplete"
#     st.metric("Status", completion)

# # Checklist
# st.subheader("✅ Completion Checklist")
# col1, col2 = st.columns(2)

# with col1:
#     st.checkbox("Group created on platform", key="check_1")
#     st.checkbox("All members added", key="check_2")
# with col2:
#     st.checkbox("Work completed", key="check_3")
#     st.checkbox("Submission completed", key="check_4")

# # Final action buttons
# st.markdown("---")
# col1, col2, col3 = st.columns(3)

# with col1:
#     if st.button("🔄 Clear All Data", type="secondary"):
#         st.session_state.group_name = ""
#         st.session_state.members = []
#         st.session_state.notes = ""
#         st.rerun()

# with col2:
#     if st.button("💾 Export Summary"):
#         summary_text = f"""
# GROUP CREATION SUMMARY
# =====================
# Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

# Group Name: {st.session_state.group_name}

# Members ({len(st.session_state.members)}):
# {chr(10).join([f"  - {m['name']}" for m in st.session_state.members])}

# Notes:
# {st.session_state.notes}
# """
#         st.download_button(
#             label="📥 Download Summary",
#             data=summary_text,
#             file_name=f"group_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
#             mime="text/plain"
#         )

# # Footer
# st.markdown("---")
# st.caption("💡 Tip: Use this app to plan and track your group creation progress before submitting on the platform.")

import streamlit as st
import json
import os
from datetime import datetime
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Group Management System",
    page_icon="👥",
    layout="wide"
)

# File path for persistent storage
STORAGE_FILE = Path("groups_data.json")

# Initialize session state
if 'groups' not in st.session_state:
    st.session_state.groups = {}
if 'selected_group_id' not in st.session_state:
    st.session_state.selected_group_id = None
if 'initialized' not in st.session_state:
    st.session_state.initialized = False

# Load data from file
def load_data():
    """Load groups data from JSON file"""
    if STORAGE_FILE.exists():
        try:
            with open(STORAGE_FILE, 'r') as f:
                data = json.load(f)
                st.session_state.groups = data.get('groups', {})
                if st.session_state.groups and not st.session_state.selected_group_id:
                    st.session_state.selected_group_id = list(st.session_state.groups.keys())[0]
        except Exception as e:
            st.error(f"Error loading data: {e}")

# Save data to file
def save_data():
    """Save groups data to JSON file"""
    try:
        with open(STORAGE_FILE, 'w') as f:
            json.dump({'groups': st.session_state.groups}, f, indent=2)
        return True
    except Exception as e:
        st.error(f"Error saving data: {e}")
        return False

# Load data on first run
if not st.session_state.initialized:
    load_data()
    st.session_state.initialized = True

# Helper functions
def create_group(group_name):
    """Create a new group"""
    if not group_name.strip():
        st.error("Group name cannot be empty")
        return False
    
    group_id = f"grp_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    st.session_state.groups[group_id] = {
        'id': group_id,
        'name': group_name.strip(),
        'members': {},
        'created_at': datetime.now().isoformat()
    }
    st.session_state.selected_group_id = group_id
    save_data()
    return True

def delete_group(group_id):
    """Delete a group"""
    if group_id in st.session_state.groups:
        del st.session_state.groups[group_id]
        if st.session_state.selected_group_id == group_id:
            if st.session_state.groups:
                st.session_state.selected_group_id = list(st.session_state.groups.keys())[0]
            else:
                st.session_state.selected_group_id = None
        save_data()
        return True
    return False

def add_member(group_id, name, email):
    """Add a member to a group"""
    if not name.strip() or not email.strip():
        st.error("Both name and email are required")
        return False
    
    if group_id not in st.session_state.groups:
        return False
    
    member_id = f"mem_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}"
    st.session_state.groups[group_id]['members'][member_id] = {
        'id': member_id,
        'name': name.strip(),
        'email': email.strip(),
        'comments': [],
        'added_at': datetime.now().isoformat()
    }
    save_data()
    return True

def delete_member(group_id, member_id):
    """Delete a member from a group"""
    if group_id in st.session_state.groups:
        if member_id in st.session_state.groups[group_id]['members']:
            del st.session_state.groups[group_id]['members'][member_id]
            save_data()
            return True
    return False

def add_comment(group_id, member_id, comment_text):
    """Add a comment to a member"""
    if not comment_text.strip():
        return False
    
    if group_id in st.session_state.groups:
        if member_id in st.session_state.groups[group_id]['members']:
            comment = {
                'id': f"cmt_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}",
                'text': comment_text.strip(),
                'timestamp': datetime.now().isoformat()
            }
            st.session_state.groups[group_id]['members'][member_id]['comments'].append(comment)
            save_data()
            return True
    return False

def delete_comment(group_id, member_id, comment_id):
    """Delete a comment from a member"""
    if group_id in st.session_state.groups:
        if member_id in st.session_state.groups[group_id]['members']:
            member = st.session_state.groups[group_id]['members'][member_id]
            member['comments'] = [c for c in member['comments'] if c['id'] != comment_id]
            save_data()
            return True
    return False

# Title
st.title("👥 Group Management System")
st.markdown("Create and manage multiple groups with member contributions")
st.markdown("---")

# Layout: Sidebar and Main Content
col_sidebar, col_main = st.columns([1, 3])

# Sidebar - Group List
with col_sidebar:
    st.subheader("📋 Groups")
    
    # Create new group
    with st.expander("➕ Create New Group", expanded=False):
        new_group_name = st.text_input("Group Name", key="new_group_name")
        if st.button("Create Group", type="primary"):
            if create_group(new_group_name):
                st.success("Group created!")
                st.rerun()
    
    st.markdown("---")
    
    # List all groups
    if st.session_state.groups:
        for group_id, group in st.session_state.groups.items():
            col1, col2 = st.columns([4, 1])
            
            with col1:
                is_selected = st.session_state.selected_group_id == group_id
                button_type = "primary" if is_selected else "secondary"
                if st.button(
                    f"{'✓ ' if is_selected else ''}{group['name']}\n({len(group['members'])} members)",
                    key=f"select_{group_id}",
                    use_container_width=True,
                    type=button_type
                ):
                    st.session_state.selected_group_id = group_id
                    st.rerun()
            
            with col2:
                if st.button("🗑️", key=f"del_{group_id}", help="Delete group"):
                    if delete_group(group_id):
                        st.rerun()
    else:
        st.info("No groups yet. Create one to get started!")

# Main Content - Group Details
with col_main:
    if st.session_state.selected_group_id and st.session_state.selected_group_id in st.session_state.groups:
        current_group = st.session_state.groups[st.session_state.selected_group_id]
        
        # Group header
        st.header(current_group['name'])
        st.caption(f"Created: {datetime.fromisoformat(current_group['created_at']).strftime('%Y-%m-%d %H:%M')}")
        st.markdown("---")
        
        # Add member form
        st.subheader("➕ Add New Member")
        with st.form("add_member_form", clear_on_submit=True):
            col1, col2, col3 = st.columns([2, 2, 1])
            with col1:
                member_name = st.text_input("Member Name", placeholder="John Doe")
            with col2:
                member_email = st.text_input("Member Email", placeholder="john@example.com")
            with col3:
                st.write("")  # Spacing
                submit_member = st.form_submit_button("Add Member", type="primary", use_container_width=True)
            
            if submit_member:
                if add_member(st.session_state.selected_group_id, member_name, member_email):
                    st.success(f"Added {member_name} to the group!")
                    st.rerun()
        
        st.markdown("---")
        
        # Members list
        st.subheader(f"👥 Members ({len(current_group['members'])})")
        
        if not current_group['members']:
            st.info("No members yet. Add members using the form above.")
        else:
            for member_id, member in current_group['members'].items():
                with st.container():
                    # Member card
                    col1, col2 = st.columns([5, 1])
                    
                    with col1:
                        st.markdown(f"**{member['name']}**")
                        st.caption(f"📧 {member['email']}")
                        st.caption(f"Added: {datetime.fromisoformat(member['added_at']).strftime('%Y-%m-%d %H:%M')}")
                    
                    with col2:
                        if st.button("🗑️", key=f"del_mem_{member_id}", help="Remove member"):
                            if delete_member(st.session_state.selected_group_id, member_id):
                                st.rerun()
                    
                    # Comments section
                    with st.expander(f"💬 Comments ({len(member['comments'])})", expanded=False):
                        # Add comment
                        comment_text = st.text_area(
                            "Add a comment about their contribution",
                            key=f"comment_input_{member_id}",
                            placeholder="e.g., Completed the frontend design..."
                        )
                        
                        col_add, col_space = st.columns([1, 3])
                        with col_add:
                            if st.button("Add Comment", key=f"add_cmt_{member_id}"):
                                if add_comment(st.session_state.selected_group_id, member_id, comment_text):
                                    st.success("Comment added!")
                                    st.rerun()
                        
                        # Display comments
                        if member['comments']:
                            st.markdown("**Previous Comments:**")
                            for idx, comment in enumerate(reversed(member['comments'])):
                                with st.container():
                                    col_cmt, col_del = st.columns([5, 1])
                                    with col_cmt:
                                        st.markdown(f"_{comment['text']}_")
                                        st.caption(f"🕒 {datetime.fromisoformat(comment['timestamp']).strftime('%Y-%m-%d %H:%M:%S')}")
                                    with col_del:
                                        if st.button("✖", key=f"del_cmt_{comment['id']}", help="Delete comment"):
                                            if delete_comment(st.session_state.selected_group_id, member_id, comment['id']):
                                                st.rerun()
                                    st.markdown("---")
                        else:
                            st.info("No comments yet")
                    
                    st.markdown("---")
        
        # Export group data
        st.markdown("---")
        st.subheader("💾 Export Group Data")
        
        export_data = {
            'group_name': current_group['name'],
            'created_at': current_group['created_at'],
            'members': []
        }
        
        for member in current_group['members'].values():
            export_data['members'].append({
                'name': member['name'],
                'email': member['email'],
                'comments': [c['text'] for c in member['comments']],
                'added_at': member['added_at']
            })
        
        st.download_button(
            label="📥 Download Group Data (JSON)",
            data=json.dumps(export_data, indent=2),
            file_name=f"{current_group['name'].replace(' ', '_')}_data.json",
            mime="application/json"
        )
    
    else:
        # No group selected
        st.info("👈 Select a group from the sidebar or create a new one to get started!")
        
        # Display statistics
        if st.session_state.groups:
            st.markdown("---")
            st.subheader("📊 Overview")
            
            total_members = sum(len(g['members']) for g in st.session_state.groups.values())
            total_comments = sum(
                len(m['comments']) 
                for g in st.session_state.groups.values() 
                for m in g['members'].values()
            )
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Groups", len(st.session_state.groups))
            with col2:
                st.metric("Total Members", total_members)
            with col3:
                st.metric("Total Comments", total_comments)

# Footer
st.markdown("---")
st.caption("💡 All data is automatically saved and persists between sessions")
st.caption(f"📁 Storage file: {STORAGE_FILE.absolute()}")