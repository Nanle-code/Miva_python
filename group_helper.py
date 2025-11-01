# # import streamlit as st
# # import json
# # import os
# # from datetime import datetime
# # from pathlib import Path

# # # Page configuration
# # st.set_page_config(
# #     page_title="Group Management System",
# #     page_icon="👥",
# #     layout="wide"
# # )

# # # File path for persistent storage
# # STORAGE_FILE = Path("groups_data.json")

# # # Initialize session state
# # if 'groups' not in st.session_state:
# #     st.session_state.groups = {}
# # if 'selected_group_id' not in st.session_state:
# #     st.session_state.selected_group_id = None
# # if 'initialized' not in st.session_state:
# #     st.session_state.initialized = False

# # # Load data from file
# # def load_data():
# #     """Load groups data from JSON file"""
# #     if STORAGE_FILE.exists():
# #         try:
# #             with open(STORAGE_FILE, 'r') as f:
# #                 data = json.load(f)
# #                 st.session_state.groups = data.get('groups', {})
# #                 if st.session_state.groups and not st.session_state.selected_group_id:
# #                     st.session_state.selected_group_id = list(st.session_state.groups.keys())[0]
# #         except Exception as e:
# #             st.error(f"Error loading data: {e}")

# # # Save data to file
# # def save_data():
# #     """Save groups data to JSON file"""
# #     try:
# #         with open(STORAGE_FILE, 'w') as f:
# #             json.dump({'groups': st.session_state.groups}, f, indent=2)
# #         return True
# #     except Exception as e:
# #         st.error(f"Error saving data: {e}")
# #         return False

# # # Load data on first run
# # if not st.session_state.initialized:
# #     load_data()
# #     st.session_state.initialized = True

# # # Helper functions
# # def create_group(group_name):
# #     """Create a new group"""
# #     if not group_name.strip():
# #         st.error("Group name cannot be empty")
# #         return False
    
# #     group_id = f"grp_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
# #     st.session_state.groups[group_id] = {
# #         'id': group_id,
# #         'name': group_name.strip(),
# #         'members': {},
# #         'created_at': datetime.now().isoformat()
# #     }
# #     st.session_state.selected_group_id = group_id
# #     save_data()
# #     return True

# # def delete_group(group_id):
# #     """Delete a group"""
# #     if group_id in st.session_state.groups:
# #         del st.session_state.groups[group_id]
# #         if st.session_state.selected_group_id == group_id:
# #             if st.session_state.groups:
# #                 st.session_state.selected_group_id = list(st.session_state.groups.keys())[0]
# #             else:
# #                 st.session_state.selected_group_id = None
# #         save_data()
# #         return True
# #     return False

# # def add_member(group_id, name, email):
# #     """Add a member to a group"""
# #     if not name.strip() or not email.strip():
# #         st.error("Both name and email are required")
# #         return False
    
# #     if group_id not in st.session_state.groups:
# #         return False
    
# #     member_id = f"mem_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}"
# #     st.session_state.groups[group_id]['members'][member_id] = {
# #         'id': member_id,
# #         'name': name.strip(),
# #         'email': email.strip(),
# #         'comments': [],
# #         'added_at': datetime.now().isoformat()
# #     }
# #     save_data()
# #     return True

# # def delete_member(group_id, member_id):
# #     """Delete a member from a group"""
# #     if group_id in st.session_state.groups:
# #         if member_id in st.session_state.groups[group_id]['members']:
# #             del st.session_state.groups[group_id]['members'][member_id]
# #             save_data()
# #             return True
# #     return False

# # def add_comment(group_id, member_id, comment_text):
# #     """Add a comment to a member"""
# #     if not comment_text.strip():
# #         return False
    
# #     if group_id in st.session_state.groups:
# #         if member_id in st.session_state.groups[group_id]['members']:
# #             comment = {
# #                 'id': f"cmt_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}",
# #                 'text': comment_text.strip(),
# #                 'timestamp': datetime.now().isoformat()
# #             }
# #             st.session_state.groups[group_id]['members'][member_id]['comments'].append(comment)
# #             save_data()
# #             return True
# #     return False

# # def delete_comment(group_id, member_id, comment_id):
# #     """Delete a comment from a member"""
# #     if group_id in st.session_state.groups:
# #         if member_id in st.session_state.groups[group_id]['members']:
# #             member = st.session_state.groups[group_id]['members'][member_id]
# #             member['comments'] = [c for c in member['comments'] if c['id'] != comment_id]
# #             save_data()
# #             return True
# #     return False

# # # Title
# # st.title("👥 Group Management System")
# # st.markdown("Create and manage multiple groups with member contributions")
# # st.markdown("---")

# # # Layout: Sidebar and Main Content
# # col_sidebar, col_main = st.columns([1, 3])

# # # Sidebar - Group List
# # with col_sidebar:
# #     st.subheader("📋 Groups")
    
# #     # Create new group
# #     with st.expander("➕ Create New Group", expanded=False):
# #         new_group_name = st.text_input("Group Name", key="new_group_name")
# #         if st.button("Create Group", type="primary"):
# #             if create_group(new_group_name):
# #                 st.success("Group created!")
# #                 st.rerun()
    
# #     st.markdown("---")
    
# #     # List all groups
# #     if st.session_state.groups:
# #         for group_id, group in st.session_state.groups.items():
# #             col1, col2 = st.columns([4, 1])
            
# #             with col1:
# #                 is_selected = st.session_state.selected_group_id == group_id
# #                 button_type = "primary" if is_selected else "secondary"
# #                 if st.button(
# #                     f"{'✓ ' if is_selected else ''}{group['name']}\n({len(group['members'])} members)",
# #                     key=f"select_{group_id}",
# #                     use_container_width=True,
# #                     type=button_type
# #                 ):
# #                     st.session_state.selected_group_id = group_id
# #                     st.rerun()
            
# #             with col2:
# #                 if st.button("🗑️", key=f"del_{group_id}", help="Delete group"):
# #                     if delete_group(group_id):
# #                         st.rerun()
# #     else:
# #         st.info("No groups yet. Create one to get started!")

# # # Main Content - Group Details
# # with col_main:
# #     if st.session_state.selected_group_id and st.session_state.selected_group_id in st.session_state.groups:
# #         current_group = st.session_state.groups[st.session_state.selected_group_id]
        
# #         # Group header
# #         st.header(current_group['name'])
# #         st.caption(f"Created: {datetime.fromisoformat(current_group['created_at']).strftime('%Y-%m-%d %H:%M')}")
# #         st.markdown("---")
        
# #         # Add member form
# #         st.subheader("➕ Add New Member")
# #         with st.form("add_member_form", clear_on_submit=True):
# #             col1, col2, col3 = st.columns([2, 2, 1])
# #             with col1:
# #                 member_name = st.text_input("Member Name", placeholder="John Doe")
# #             with col2:
# #                 member_email = st.text_input("Member Email", placeholder="john@example.com")
# #             with col3:
# #                 st.write("")  # Spacing
# #                 submit_member = st.form_submit_button("Add Member", type="primary", use_container_width=True)
            
# #             if submit_member:
# #                 if add_member(st.session_state.selected_group_id, member_name, member_email):
# #                     st.success(f"Added {member_name} to the group!")
# #                     st.rerun()
        
# #         st.markdown("---")
        
# #         # Members list
# #         st.subheader(f"👥 Members ({len(current_group['members'])})")
        
# #         if not current_group['members']:
# #             st.info("No members yet. Add members using the form above.")
# #         else:
# #             for member_id, member in current_group['members'].items():
# #                 with st.container():
# #                     # Member card
# #                     col1, col2 = st.columns([5, 1])
                    
# #                     with col1:
# #                         st.markdown(f"**{member['name']}**")
# #                         st.caption(f"📧 {member['email']}")
# #                         st.caption(f"Added: {datetime.fromisoformat(member['added_at']).strftime('%Y-%m-%d %H:%M')}")
                    
# #                     with col2:
# #                         if st.button("🗑️", key=f"del_mem_{member_id}", help="Remove member"):
# #                             if delete_member(st.session_state.selected_group_id, member_id):
# #                                 st.rerun()
                    
# #                     # Comments section
# #                     with st.expander(f"💬 Comments ({len(member['comments'])})", expanded=False):
# #                         # Add comment
# #                         comment_text = st.text_area(
# #                             "Add a comment about their contribution",
# #                             key=f"comment_input_{member_id}",
# #                             placeholder="e.g., Completed the frontend design..."
# #                         )
                        
# #                         col_add, col_space = st.columns([1, 3])
# #                         with col_add:
# #                             if st.button("Add Comment", key=f"add_cmt_{member_id}"):
# #                                 if add_comment(st.session_state.selected_group_id, member_id, comment_text):
# #                                     st.success("Comment added!")
# #                                     st.rerun()
                        
# #                         # Display comments
# #                         if member['comments']:
# #                             st.markdown("**Previous Comments:**")
# #                             for idx, comment in enumerate(reversed(member['comments'])):
# #                                 with st.container():
# #                                     col_cmt, col_del = st.columns([5, 1])
# #                                     with col_cmt:
# #                                         st.markdown(f"_{comment['text']}_")
# #                                         st.caption(f"🕒 {datetime.fromisoformat(comment['timestamp']).strftime('%Y-%m-%d %H:%M:%S')}")
# #                                     with col_del:
# #                                         if st.button("✖", key=f"del_cmt_{comment['id']}", help="Delete comment"):
# #                                             if delete_comment(st.session_state.selected_group_id, member_id, comment['id']):
# #                                                 st.rerun()
# #                                     st.markdown("---")
# #                         else:
# #                             st.info("No comments yet")
                    
# #                     st.markdown("---")
        
# #         # Export group data
# #         st.markdown("---")
# #         st.subheader("💾 Export Group Data")
        
# #         export_data = {
# #             'group_name': current_group['name'],
# #             'created_at': current_group['created_at'],
# #             'members': []
# #         }
        
# #         for member in current_group['members'].values():
# #             export_data['members'].append({
# #                 'name': member['name'],
# #                 'email': member['email'],
# #                 'comments': [c['text'] for c in member['comments']],
# #                 'added_at': member['added_at']
# #             })
        
# #         st.download_button(
# #             label="📥 Download Group Data (JSON)",
# #             data=json.dumps(export_data, indent=2),
# #             file_name=f"{current_group['name'].replace(' ', '_')}_data.json",
# #             mime="application/json"
# #         )
    
# #     else:
# #         # No group selected
# #         st.info("👈 Select a group from the sidebar or create a new one to get started!")
        
# #         # Display statistics
# #         if st.session_state.groups:
# #             st.markdown("---")
# #             st.subheader("📊 Overview")
            
# #             total_members = sum(len(g['members']) for g in st.session_state.groups.values())
# #             total_comments = sum(
# #                 len(m['comments']) 
# #                 for g in st.session_state.groups.values() 
# #                 for m in g['members'].values()
# #             )
            
# #             col1, col2, col3 = st.columns(3)
# #             with col1:
# #                 st.metric("Total Groups", len(st.session_state.groups))
# #             with col2:
# #                 st.metric("Total Members", total_members)
# #             with col3:
# #                 st.metric("Total Comments", total_comments)

# # # Footer
# # st.markdown("---")
# # st.caption("💡 All data is automatically saved and persists between sessions")
# # st.caption(f"📁 Storage file: {STORAGE_FILE.absolute()}")


# import streamlit as st
# import json
# import os
# from datetime import datetime
# from pathlib import Path
# import hashlib

# # Page configuration
# st.set_page_config(
#     page_title="Group Management System",
#     page_icon="👥",
#     layout="wide"
# )

# # File paths for persistent storage
# STORAGE_FILE = Path("groups_data.json")
# USERS_FILE = Path("users_data.json")

# # Initialize session state
# if 'groups' not in st.session_state:
#     st.session_state.groups = {}
# if 'users' not in st.session_state:
#     st.session_state.users = {}
# if 'selected_group_id' not in st.session_state:
#     st.session_state.selected_group_id = None
# if 'initialized' not in st.session_state:
#     st.session_state.initialized = False
# if 'logged_in_user' not in st.session_state:
#     st.session_state.logged_in_user = None
# if 'user_role' not in st.session_state:
#     st.session_state.user_role = None

# # Hash password for security
# def hash_password(password):
#     return hashlib.sha256(password.encode()).hexdigest()

# # Load data from files
# def load_data():
#     """Load groups and users data from JSON files"""
#     # Load groups
#     if STORAGE_FILE.exists():
#         try:
#             with open(STORAGE_FILE, 'r') as f:
#                 data = json.load(f)
#                 st.session_state.groups = data.get('groups', {})
#         except Exception as e:
#             st.error(f"Error loading groups data: {e}")
    
#     # Load users
#     if USERS_FILE.exists():
#         try:
#             with open(USERS_FILE, 'r') as f:
#                 st.session_state.users = json.load(f)
#         except Exception as e:
#             st.error(f"Error loading users data: {e}")

# # Save data to files
# def save_groups_data():
#     """Save groups data to JSON file"""
#     try:
#         with open(STORAGE_FILE, 'w') as f:
#             json.dump({'groups': st.session_state.groups}, f, indent=2)
#         return True
#     except Exception as e:
#         st.error(f"Error saving groups data: {e}")
#         return False

# def save_users_data():
#     """Save users data to JSON file"""
#     try:
#         with open(USERS_FILE, 'w') as f:
#             json.dump(st.session_state.users, f, indent=2)
#         return True
#     except Exception as e:
#         st.error(f"Error saving users data: {e}")
#         return False

# # Load data on first run
# if not st.session_state.initialized:
#     load_data()
#     st.session_state.initialized = True

# # User management functions
# def register_user(email, password, name):
#     """Register a new user"""
#     if email in st.session_state.users:
#         return False, "User already exists"
    
#     st.session_state.users[email] = {
#         'email': email,
#         'password': hash_password(password),
#         'name': name,
#         'role': 'admin',  # First user or admin
#         'created_at': datetime.now().isoformat()
#     }
#     save_users_data()
#     return True, "Registration successful"

# def login_user(email, password):
#     """Login a user"""
#     if email not in st.session_state.users:
#         return False, "User not found"
    
#     if st.session_state.users[email]['password'] != hash_password(password):
#         return False, "Incorrect password"
    
#     st.session_state.logged_in_user = email
#     st.session_state.user_role = st.session_state.users[email]['role']
#     return True, "Login successful"

# def logout_user():
#     """Logout current user"""
#     st.session_state.logged_in_user = None
#     st.session_state.user_role = None
#     st.session_state.selected_group_id = None

# def is_group_admin(group_id):
#     """Check if current user is admin of the group"""
#     if not st.session_state.logged_in_user:
#         return False
    
#     if group_id not in st.session_state.groups:
#         return False
    
#     group = st.session_state.groups[group_id]
#     return group['admin_email'] == st.session_state.logged_in_user

# def is_group_member(group_id):
#     """Check if current user is a member of the group"""
#     if not st.session_state.logged_in_user:
#         return False
    
#     if group_id not in st.session_state.groups:
#         return False
    
#     group = st.session_state.groups[group_id]
    
#     # Admin is always a member
#     if group['admin_email'] == st.session_state.logged_in_user:
#         return True
    
#     # Check if user is in members list
#     for member in group['members'].values():
#         if member['email'] == st.session_state.logged_in_user:
#             return True
    
#     return False

# # Group management functions
# def create_group(group_name):
#     """Create a new group (admin only)"""
#     if not st.session_state.logged_in_user:
#         st.error("You must be logged in to create a group")
#         return False
    
#     if not group_name.strip():
#         st.error("Group name cannot be empty")
#         return False
    
#     group_id = f"grp_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
#     st.session_state.groups[group_id] = {
#         'id': group_id,
#         'name': group_name.strip(),
#         'admin_email': st.session_state.logged_in_user,
#         'admin_name': st.session_state.users[st.session_state.logged_in_user]['name'],
#         'members': {},
#         'created_at': datetime.now().isoformat()
#     }
#     st.session_state.selected_group_id = group_id
#     save_groups_data()
#     return True

# def delete_group(group_id):
#     """Delete a group (admin only)"""
#     if not is_group_admin(group_id):
#         st.error("Only group admin can delete the group")
#         return False
    
#     if group_id in st.session_state.groups:
#         del st.session_state.groups[group_id]
#         if st.session_state.selected_group_id == group_id:
#             if st.session_state.groups:
#                 st.session_state.selected_group_id = list(st.session_state.groups.keys())[0]
#             else:
#                 st.session_state.selected_group_id = None
#         save_groups_data()
#         return True
#     return False

# def add_member(group_id, name, email):
#     """Add a member to a group (admin only)"""
#     if not is_group_admin(group_id):
#         st.error("Only group admin can add members")
#         return False
    
#     if not name.strip() or not email.strip():
#         st.error("Both name and email are required")
#         return False
    
#     if group_id not in st.session_state.groups:
#         return False
    
#     member_id = f"mem_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}"
#     st.session_state.groups[group_id]['members'][member_id] = {
#         'id': member_id,
#         'name': name.strip(),
#         'email': email.strip(),
#         'comments': [],
#         'added_at': datetime.now().isoformat()
#     }
#     save_groups_data()
#     return True

# def delete_member(group_id, member_id):
#     """Delete a member from a group (admin only)"""
#     if not is_group_admin(group_id):
#         st.error("Only group admin can remove members")
#         return False
    
#     if group_id in st.session_state.groups:
#         if member_id in st.session_state.groups[group_id]['members']:
#             del st.session_state.groups[group_id]['members'][member_id]
#             save_groups_data()
#             return True
#     return False

# def add_comment(group_id, member_id, comment_text):
#     """Add a comment to a member (members can comment)"""
#     if not is_group_member(group_id):
#         st.error("Only group members can add comments")
#         return False
    
#     if not comment_text.strip():
#         return False
    
#     if group_id in st.session_state.groups:
#         if member_id in st.session_state.groups[group_id]['members']:
#             comment = {
#                 'id': f"cmt_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}",
#                 'text': comment_text.strip(),
#                 'author': st.session_state.users[st.session_state.logged_in_user]['name'],
#                 'author_email': st.session_state.logged_in_user,
#                 'timestamp': datetime.now().isoformat()
#             }
#             st.session_state.groups[group_id]['members'][member_id]['comments'].append(comment)
#             save_groups_data()
#             return True
#     return False

# def delete_comment(group_id, member_id, comment_id):
#     """Delete a comment (admin or comment author only)"""
#     if group_id in st.session_state.groups:
#         if member_id in st.session_state.groups[group_id]['members']:
#             member = st.session_state.groups[group_id]['members'][member_id]
#             comment = next((c for c in member['comments'] if c['id'] == comment_id), None)
            
#             if comment:
#                 # Check if user is admin or comment author
#                 if is_group_admin(group_id) or comment['author_email'] == st.session_state.logged_in_user:
#                     member['comments'] = [c for c in member['comments'] if c['id'] != comment_id]
#                     save_groups_data()
#                     return True
#                 else:
#                     st.error("You can only delete your own comments")
#                     return False
#     return False

# # LOGIN/REGISTRATION PAGE
# if not st.session_state.logged_in_user:
#     st.title("🔐 Group Management System")
#     st.markdown("### Please login or register to continue")
    
#     tab1, tab2 = st.tabs(["Login", "Register"])
    
#     with tab1:
#         st.subheader("Login")
#         with st.form("login_form"):
#             login_email = st.text_input("Email", key="login_email")
#             login_password = st.text_input("Password", type="password", key="login_password")
#             login_submit = st.form_submit_button("Login", type="primary", use_container_width=True)
            
#             if login_submit:
#                 success, message = login_user(login_email, login_password)
#                 if success:
#                     st.success(message)
#                     st.rerun()
#                 else:
#                     st.error(message)
    
#     with tab2:
#         st.subheader("Register")
#         with st.form("register_form"):
#             reg_name = st.text_input("Full Name", key="reg_name")
#             reg_email = st.text_input("Email", key="reg_email")
#             reg_password = st.text_input("Password", type="password", key="reg_password")
#             reg_password2 = st.text_input("Confirm Password", type="password", key="reg_password2")
#             register_submit = st.form_submit_button("Register", type="primary", use_container_width=True)
            
#             if register_submit:
#                 if reg_password != reg_password2:
#                     st.error("Passwords do not match")
#                 elif len(reg_password) < 6:
#                     st.error("Password must be at least 6 characters")
#                 else:
#                     success, message = register_user(reg_email, reg_password, reg_name)
#                     if success:
#                         st.success(message)
#                         st.info("Please login with your credentials")
#                     else:
#                         st.error(message)

# # MAIN APPLICATION (only if logged in)
# else:
#     # Header with logout
#     col1, col2 = st.columns([4, 1])
#     with col1:
#         st.title("👥 Group Management System")
#         st.caption(f"Logged in as: **{st.session_state.users[st.session_state.logged_in_user]['name']}** ({st.session_state.logged_in_user})")
#     with col2:
#         st.write("")
#         if st.button("🚪 Logout", use_container_width=True):
#             logout_user()
#             st.rerun()
    
#     st.markdown("---")
    
#     # Layout: Sidebar and Main Content
#     col_sidebar, col_main = st.columns([1, 3])
    
#     # Sidebar - Group List
#     with col_sidebar:
#         st.subheader("📋 My Groups")
        
#         # Create new group (only show create button)
#         with st.expander("➕ Create New Group", expanded=False):
#             new_group_name = st.text_input("Group Name", key="new_group_name")
#             if st.button("Create Group", type="primary"):
#                 if create_group(new_group_name):
#                     st.success("Group created!")
#                     st.rerun()
        
#         st.markdown("---")
        
#         # Filter groups where user is admin or member
#         user_groups = {
#             gid: g for gid, g in st.session_state.groups.items()
#             if is_group_admin(gid) or is_group_member(gid)
#         }
        
#         # List all accessible groups
#         if user_groups:
#             for group_id, group in user_groups.items():
#                 col1, col2 = st.columns([4, 1])
                
#                 with col1:
#                     is_selected = st.session_state.selected_group_id == group_id
#                     is_admin = is_group_admin(group_id)
#                     button_label = f"{'✓ ' if is_selected else ''}{group['name']}"
#                     button_label += f"\n({len(group['members'])} members)"
#                     if is_admin:
#                         button_label += " 👑"
                    
#                     button_type = "primary" if is_selected else "secondary"
#                     if st.button(
#                         button_label,
#                         key=f"select_{group_id}",
#                         use_container_width=True,
#                         type=button_type
#                     ):
#                         st.session_state.selected_group_id = group_id
#                         st.rerun()
                
#                 with col2:
#                     if is_admin:
#                         if st.button("🗑️", key=f"del_{group_id}", help="Delete group"):
#                             if delete_group(group_id):
#                                 st.rerun()
#         else:
#             st.info("No groups yet. Create one to get started!")
    
#     # Main Content - Group Details
#     with col_main:
#         if st.session_state.selected_group_id and st.session_state.selected_group_id in st.session_state.groups:
#             current_group = st.session_state.groups[st.session_state.selected_group_id]
#             is_admin = is_group_admin(st.session_state.selected_group_id)
            
#             # Group header
#             col1, col2 = st.columns([3, 1])
#             with col1:
#                 st.header(current_group['name'])
#                 st.caption(f"Admin: {current_group['admin_name']} ({current_group['admin_email']})")
#                 st.caption(f"Created: {datetime.fromisoformat(current_group['created_at']).strftime('%Y-%m-%d %H:%M')}")
#             with col2:
#                 if is_admin:
#                     st.success("👑 Admin")
#                 else:
#                     st.info("👤 Member")
            
#             st.markdown("---")
            
#             # Add member form (admin only)
#             if is_admin:
#                 st.subheader("➕ Add New Member")
#                 with st.form("add_member_form", clear_on_submit=True):
#                     col1, col2, col3 = st.columns([2, 2, 1])
#                     with col1:
#                         member_name = st.text_input("Member Name", placeholder="John Doe")
#                     with col2:
#                         member_email = st.text_input("Member Email", placeholder="john@example.com")
#                     with col3:
#                         st.write("")
#                         submit_member = st.form_submit_button("Add Member", type="primary", use_container_width=True)
                    
#                     if submit_member:
#                         if add_member(st.session_state.selected_group_id, member_name, member_email):
#                             st.success(f"Added {member_name} to the group!")
#                             st.rerun()
                
#                 st.markdown("---")
            
#             # Members list
#             st.subheader(f"👥 Members ({len(current_group['members'])})")
            
#             if not current_group['members']:
#                 st.info("No members yet." + (" Add members using the form above." if is_admin else ""))
#             else:
#                 for member_id, member in current_group['members'].items():
#                     with st.container():
#                         # Member card
#                         col1, col2 = st.columns([5, 1])
                        
#                         with col1:
#                             st.markdown(f"**{member['name']}**")
#                             st.caption(f"📧 {member['email']}")
#                             st.caption(f"Added: {datetime.fromisoformat(member['added_at']).strftime('%Y-%m-%d %H:%M')}")
                        
#                         with col2:
#                             if is_admin:
#                                 if st.button("🗑️", key=f"del_mem_{member_id}", help="Remove member"):
#                                     if delete_member(st.session_state.selected_group_id, member_id):
#                                         st.rerun()
                        
#                         # Comments section (all members can view and add)
#                         with st.expander(f"💬 Comments ({len(member['comments'])})", expanded=False):
#                             # Add comment
#                             comment_text = st.text_area(
#                                 "Add a comment about their contribution",
#                                 key=f"comment_input_{member_id}",
#                                 placeholder="e.g., Completed the frontend design..."
#                             )
                            
#                             col_add, col_space = st.columns([1, 3])
#                             with col_add:
#                                 if st.button("Add Comment", key=f"add_cmt_{member_id}"):
#                                     if add_comment(st.session_state.selected_group_id, member_id, comment_text):
#                                         st.success("Comment added!")
#                                         st.rerun()
                            
#                             # Display comments
#                             if member['comments']:
#                                 st.markdown("**Previous Comments:**")
#                                 for idx, comment in enumerate(reversed(member['comments'])):
#                                     with st.container():
#                                         col_cmt, col_del = st.columns([5, 1])
#                                         with col_cmt:
#                                             st.markdown(f"_{comment['text']}_")
#                                             st.caption(f"👤 {comment['author']} | 🕒 {datetime.fromisoformat(comment['timestamp']).strftime('%Y-%m-%d %H:%M:%S')}")
#                                         with col_del:
#                                             # Show delete button if user is admin or comment author
#                                             if is_admin or comment['author_email'] == st.session_state.logged_in_user:
#                                                 if st.button("✖", key=f"del_cmt_{comment['id']}", help="Delete comment"):
#                                                     if delete_comment(st.session_state.selected_group_id, member_id, comment['id']):
#                                                         st.rerun()
#                                         st.markdown("---")
#                             else:
#                                 st.info("No comments yet")
                        
#                         st.markdown("---")
            
#             # Export group data (admin only)
#             if is_admin:
#                 st.markdown("---")
#                 st.subheader("💾 Export Group Data")
                
#                 export_data = {
#                     'group_name': current_group['name'],
#                     'admin': current_group['admin_name'],
#                     'created_at': current_group['created_at'],
#                     'members': []
#                 }
                
#                 for member in current_group['members'].values():
#                     export_data['members'].append({
#                         'name': member['name'],
#                         'email': member['email'],
#                         'comments': [{'text': c['text'], 'author': c['author'], 'timestamp': c['timestamp']} for c in member['comments']],
#                         'added_at': member['added_at']
#                     })
                
#                 st.download_button(
#                     label="📥 Download Group Data (JSON)",
#                     data=json.dumps(export_data, indent=2),
#                     file_name=f"{current_group['name'].replace(' ', '_')}_data.json",
#                     mime="application/json"
#                 )
        
#         else:
#             # No group selected
#             st.info("👈 Select a group from the sidebar or create a new one to get started!")
    
#     # Footer
#     st.markdown("---")
#     st.caption("💡 All data is automatically saved and persists between sessions")
#     st.caption(f"📁 Storage files: {STORAGE_FILE.absolute()} | {USERS_FILE.absolute()}")

import streamlit as st
import json
import os
from datetime import datetime
from pathlib import Path
import hashlib

# Page configuration
st.set_page_config(
    page_title="Group Management System",
    page_icon="👥",
    layout="wide"
)

# File paths for persistent storage
STORAGE_FILE = Path("groups_data.json")
USERS_FILE = Path("users_data.json")

# Initialize session state
if 'groups' not in st.session_state:
    st.session_state.groups = {}
if 'users' not in st.session_state:
    st.session_state.users = {}
if 'selected_group_id' not in st.session_state:
    st.session_state.selected_group_id = None
if 'initialized' not in st.session_state:
    st.session_state.initialized = False
if 'logged_in_user' not in st.session_state:
    st.session_state.logged_in_user = None
if 'user_role' not in st.session_state:
    st.session_state.user_role = None

# Hash password for security
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Load data from files
def load_data():
    """Load groups and users data from JSON files"""
    # Load groups
    if STORAGE_FILE.exists():
        try:
            with open(STORAGE_FILE, 'r') as f:
                data = json.load(f)
                st.session_state.groups = data.get('groups', {})
        except Exception as e:
            st.error(f"Error loading groups data: {e}")
    
    # Load users
    if USERS_FILE.exists():
        try:
            with open(USERS_FILE, 'r') as f:
                st.session_state.users = json.load(f)
        except Exception as e:
            st.error(f"Error loading users data: {e}")

# Save data to files
def save_groups_data():
    """Save groups data to JSON file"""
    try:
        with open(STORAGE_FILE, 'w') as f:
            json.dump({'groups': st.session_state.groups}, f, indent=2)
        return True
    except Exception as e:
        st.error(f"Error saving groups data: {e}")
        return False

def save_users_data():
    """Save users data to JSON file"""
    try:
        with open(USERS_FILE, 'w') as f:
            json.dump(st.session_state.users, f, indent=2)
        return True
    except Exception as e:
        st.error(f"Error saving users data: {e}")
        return False

# Load data on first run
if not st.session_state.initialized:
    load_data()
    st.session_state.initialized = True

# User management functions
def register_user(email, password, name):
    """Register a new user"""
    if email in st.session_state.users:
        return False, "User already exists"
    
    st.session_state.users[email] = {
        'email': email,
        'password': hash_password(password),
        'name': name,
        'created_at': datetime.now().isoformat()
    }
    save_users_data()
    return True, "Registration successful"

def login_user(email, password):
    """Login a user"""
    if email not in st.session_state.users:
        return False, "User not found. Please register first."
    
    if st.session_state.users[email]['password'] != hash_password(password):
        return False, "Incorrect password"
    
    st.session_state.logged_in_user = email
    return True, "Login successful"

def logout_user():
    """Logout current user"""
    st.session_state.logged_in_user = None
    st.session_state.user_role = None
    st.session_state.selected_group_id = None

def is_group_admin(group_id):
    """Check if current user is admin of the group"""
    if not st.session_state.logged_in_user:
        return False
    
    if group_id not in st.session_state.groups:
        return False
    
    group = st.session_state.groups[group_id]
    return group.get('admin_email') == st.session_state.logged_in_user

def can_access_group(group_id):
    """Check if current user can access the group (admin or added member)"""
    if not st.session_state.logged_in_user:
        return False
    
    if group_id not in st.session_state.groups:
        return False
    
    group = st.session_state.groups[group_id]
    
    # Admin can always access
    if group.get('admin_email') == st.session_state.logged_in_user:
        return True
    
    # Check if user email is in the members list
    for member in group['members'].values():
        if member['email'].lower() == st.session_state.logged_in_user.lower():
            return True
    
    return False

def get_accessible_groups():
    """Get all groups the current user can access"""
    if not st.session_state.logged_in_user:
        return {}
    
    accessible = {}
    for group_id, group in st.session_state.groups.items():
        if can_access_group(group_id):
            accessible[group_id] = group
    
    return accessible

def get_all_groups_for_display():
    """Get all groups for display with access status"""
    if not st.session_state.logged_in_user:
        return []
    
    groups_display = []
    for group_id, group in st.session_state.groups.items():
        has_access = can_access_group(group_id)
        is_admin = is_group_admin(group_id)
        
        groups_display.append({
            'id': group_id,
            'name': group['name'],
            'admin_name': group.get('admin_name', 'Unknown'),
            'admin_email': group.get('admin_email', 'Unknown'),
            'member_count': len(group['members']),
            'has_access': has_access,
            'is_admin': is_admin,
            'created_at': group['created_at']
        })
    
    return groups_display

# Group management functions
def create_group(group_name):
    """Create a new group (any registered user can create)"""
    if not st.session_state.logged_in_user:
        st.error("You must be logged in to create a group")
        return False
    
    if not group_name.strip():
        st.error("Group name cannot be empty")
        return False
    
    group_id = f"grp_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    st.session_state.groups[group_id] = {
        'id': group_id,
        'name': group_name.strip(),
        'admin_email': st.session_state.logged_in_user,
        'admin_name': st.session_state.users[st.session_state.logged_in_user]['name'],
        'members': {},
        'created_at': datetime.now().isoformat()
    }
    st.session_state.selected_group_id = group_id
    save_groups_data()
    return True

def delete_group(group_id):
    """Delete a group (admin only)"""
    if not is_group_admin(group_id):
        st.error("Only group admin can delete the group")
        return False
    
    if group_id in st.session_state.groups:
        del st.session_state.groups[group_id]
        if st.session_state.selected_group_id == group_id:
            accessible = get_accessible_groups()
            if accessible:
                st.session_state.selected_group_id = list(accessible.keys())[0]
            else:
                st.session_state.selected_group_id = None
        save_groups_data()
        return True
    return False

def add_member(group_id, name, email):
    """Add a member to a group (admin only)"""
    if not is_group_admin(group_id):
        st.error("Only group admin can add members")
        return False
    
    if not name.strip() or not email.strip():
        st.error("Both name and email are required")
        return False
    
    if group_id not in st.session_state.groups:
        return False
    
    # Check if member already exists
    for member in st.session_state.groups[group_id]['members'].values():
        if member['email'].lower() == email.lower():
            st.warning("This member is already in the group")
            return False
    
    member_id = f"mem_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}"
    st.session_state.groups[group_id]['members'][member_id] = {
        'id': member_id,
        'name': name.strip(),
        'email': email.strip().lower(),
        'comments': [],
        'added_at': datetime.now().isoformat()
    }
    save_groups_data()
    return True

def delete_member(group_id, member_id):
    """Delete a member from a group (admin only)"""
    if not is_group_admin(group_id):
        st.error("Only group admin can remove members")
        return False
    
    if group_id in st.session_state.groups:
        if member_id in st.session_state.groups[group_id]['members']:
            del st.session_state.groups[group_id]['members'][member_id]
            save_groups_data()
            return True
    return False

def add_comment(group_id, member_id, comment_text):
    """Add a comment to a member (only users with access)"""
    if not can_access_group(group_id):
        st.error("You don't have access to this group")
        return False
    
    if not comment_text.strip():
        return False
    
    if group_id in st.session_state.groups:
        if member_id in st.session_state.groups[group_id]['members']:
            comment = {
                'id': f"cmt_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}",
                'text': comment_text.strip(),
                'author': st.session_state.users[st.session_state.logged_in_user]['name'],
                'author_email': st.session_state.logged_in_user,
                'timestamp': datetime.now().isoformat()
            }
            st.session_state.groups[group_id]['members'][member_id]['comments'].append(comment)
            save_groups_data()
            return True
    return False

def delete_comment(group_id, member_id, comment_id):
    """Delete a comment (admin or comment author only)"""
    if group_id in st.session_state.groups:
        if member_id in st.session_state.groups[group_id]['members']:
            member = st.session_state.groups[group_id]['members'][member_id]
            comment = next((c for c in member['comments'] if c['id'] == comment_id), None)
            
            if comment:
                # Check if user is admin or comment author
                if is_group_admin(group_id) or comment['author_email'] == st.session_state.logged_in_user:
                    member['comments'] = [c for c in member['comments'] if c['id'] != comment_id]
                    save_groups_data()
                    return True
                else:
                    st.error("You can only delete your own comments")
                    return False
    return False

# LOGIN/REGISTRATION PAGE
if not st.session_state.logged_in_user:
    st.title("🔐 Group Management System")
    st.markdown("### Welcome! Please register or login to continue")
    st.info("ℹ️ You must register to create groups and manage your team members")
    
    tab1, tab2 = st.tabs(["Login", "Register"])
    
    with tab1:
        st.subheader("Login to Your Account")
        with st.form("login_form"):
            login_email = st.text_input("Email", key="login_email", placeholder="your.email@example.com")
            login_password = st.text_input("Password", type="password", key="login_password")
            login_submit = st.form_submit_button("Login", type="primary", use_container_width=True)
            
            if login_submit:
                success, message = login_user(login_email, login_password)
                if success:
                    st.success(message)
                    st.rerun()
                else:
                    st.error(message)
    
    with tab2:
        st.subheader("Create New Account")
        st.info("Register to create groups and become a group admin")
        with st.form("register_form"):
            reg_name = st.text_input("Full Name", key="reg_name", placeholder="John Doe")
            reg_email = st.text_input("Email", key="reg_email", placeholder="your.email@example.com")
            reg_password = st.text_input("Password", type="password", key="reg_password")
            reg_password2 = st.text_input("Confirm Password", type="password", key="reg_password2")
            register_submit = st.form_submit_button("Register", type="primary", use_container_width=True)
            
            if register_submit:
                if reg_password != reg_password2:
                    st.error("Passwords do not match")
                elif len(reg_password) < 6:
                    st.error("Password must be at least 6 characters")
                else:
                    success, message = register_user(reg_email, reg_password, reg_name)
                    if success:
                        st.success(message)
                        st.info("✅ Registration successful! Please login with your credentials")
                    else:
                        st.error(message)

# MAIN APPLICATION (only if logged in)
else:
    # Header with logout
    col1, col2 = st.columns([4, 1])
    with col1:
        st.title("👥 Group Management System")
        st.caption(f"Logged in as: **{st.session_state.users[st.session_state.logged_in_user]['name']}** ({st.session_state.logged_in_user})")
    with col2:
        st.write("")
        if st.button("🚪 Logout", use_container_width=True):
            logout_user()
            st.rerun()
    
    st.markdown("---")
    
    # Create tabs for different views
    tab1, tab2 = st.tabs(["📂 My Groups", "🌐 All Groups"])
    
    with tab1:
        # MY GROUPS VIEW - Only groups user has access to
        col_sidebar, col_main = st.columns([1, 3])
        
        # Sidebar - My Groups List
        with col_sidebar:
            st.subheader("📋 My Groups")
            
            # Create new group
            with st.expander("➕ Create New Group", expanded=False):
                new_group_name = st.text_input("Group Name", key="new_group_name")
                if st.button("Create Group", type="primary"):
                    if create_group(new_group_name):
                        st.success("Group created! You are the admin.")
                        st.rerun()
            
            st.markdown("---")
            
            # Get accessible groups
            accessible_groups = get_accessible_groups()
            
            # List accessible groups
            if accessible_groups:
                for group_id, group in accessible_groups.items():
                    col1, col2 = st.columns([4, 1])
                    
                    with col1:
                        is_selected = st.session_state.selected_group_id == group_id
                        is_admin = is_group_admin(group_id)
                        button_label = f"{'✓ ' if is_selected else ''}{group['name']}"
                        button_label += f"\n({len(group['members'])} members)"
                        if is_admin:
                            button_label += " 👑"
                        
                        button_type = "primary" if is_selected else "secondary"
                        if st.button(
                            button_label,
                            key=f"select_{group_id}",
                            use_container_width=True,
                            type=button_type
                        ):
                            st.session_state.selected_group_id = group_id
                            st.rerun()
                    
                    with col2:
                        if is_admin:
                            if st.button("🗑️", key=f"del_{group_id}", help="Delete group"):
                                if delete_group(group_id):
                                    st.rerun()
            else:
                st.info("You don't have access to any groups yet.\n\n• Create a new group to get started\n• Or wait for a group admin to add you")
        
        # Main Content - Group Details
        with col_main:
            if st.session_state.selected_group_id and st.session_state.selected_group_id in st.session_state.groups:
                current_group = st.session_state.groups[st.session_state.selected_group_id]
                
                # Check if user still has access
                if not can_access_group(st.session_state.selected_group_id):
                    st.error("⛔ You don't have access to this group")
                    st.session_state.selected_group_id = None
                    st.rerun()
                
                is_admin = is_group_admin(st.session_state.selected_group_id)
                
                # Group header
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.header(current_group['name'])
                    admin_name = current_group.get('admin_name', 'Unknown')
                    admin_email = current_group.get('admin_email', 'Unknown')
                    st.caption(f"Admin: {admin_name} ({admin_email})")
                    st.caption(f"Created: {datetime.fromisoformat(current_group['created_at']).strftime('%Y-%m-%d %H:%M')}")
                with col2:
                    if is_admin:
                        st.success("👑 Admin")
                    else:
                        st.info("👤 Member")
                
                st.markdown("---")
                
                # Add member form (admin only)
                if is_admin:
                    st.subheader("➕ Add New Member")
                    st.caption("Add team members by their email. They can login to view and collaborate on this group.")
                    with st.form("add_member_form", clear_on_submit=True):
                        col1, col2, col3 = st.columns([2, 2, 1])
                        with col1:
                            member_name = st.text_input("Member Name", placeholder="John Doe")
                        with col2:
                            member_email = st.text_input("Member Email", placeholder="john@example.com")
                        with col3:
                            st.write("")
                            submit_member = st.form_submit_button("Add Member", type="primary", use_container_width=True)
                        
                        if submit_member:
                            if add_member(st.session_state.selected_group_id, member_name, member_email):
                                st.success(f"✅ Added {member_name} to the group! They can now access this group when they login.")
                                st.rerun()
                    
                    st.markdown("---")
                
                # Members list
                st.subheader(f"👥 Team Members ({len(current_group['members'])})")
                
                if not current_group['members']:
                    st.info("No members yet." + (" Add members using the form above." if is_admin else ""))
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
                                if is_admin:
                                    if st.button("🗑️", key=f"del_mem_{member_id}", help="Remove member"):
                                        if delete_member(st.session_state.selected_group_id, member_id):
                                            st.rerun()
                            
                            # Comments section
                            with st.expander(f"💬 Contribution Comments ({len(member['comments'])})", expanded=False):
                                # Add comment
                                comment_text = st.text_area(
                                    "Add a comment about their contribution",
                                    key=f"comment_input_{member_id}",
                                    placeholder="e.g., Completed the frontend design and implemented user authentication..."
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
                                                st.caption(f"👤 {comment['author']} | 🕒 {datetime.fromisoformat(comment['timestamp']).strftime('%Y-%m-%d %H:%M:%S')}")
                                            with col_del:
                                                # Show delete button if user is admin or comment author
                                                if is_admin or comment['author_email'] == st.session_state.logged_in_user:
                                                    if st.button("✖", key=f"del_cmt_{comment['id']}", help="Delete comment"):
                                                        if delete_comment(st.session_state.selected_group_id, member_id, comment['id']):
                                                            st.rerun()
                                            st.markdown("---")
                                else:
                                    st.info("No comments yet. Add a comment to document this member's contributions.")
                            
                            st.markdown("---")
                
                # Export group data (admin only)
                if is_admin:
                    st.markdown("---")
                    st.subheader("💾 Export Group Data")
                    
                    export_data = {
                        'group_name': current_group['name'],
                        'admin': current_group.get('admin_name', 'Unknown'),
                        'created_at': current_group['created_at'],
                        'members': []
                    }
                    
                    for member in current_group['members'].values():
                        export_data['members'].append({
                            'name': member['name'],
                            'email': member['email'],
                            'comments': [{'text': c['text'], 'author': c['author'], 'timestamp': c['timestamp']} for c in member['comments']],
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
                st.info("👈 Select a group from the sidebar to view its details")
                
                # Display statistics
                accessible_groups = get_accessible_groups()
                if accessible_groups:
                    st.markdown("---")
                    st.subheader("📊 Your Groups Overview")
                    
                    admin_count = sum(1 for gid in accessible_groups if is_group_admin(gid))
                    member_count = len(accessible_groups) - admin_count
                    total_members = sum(len(g['members']) for g in accessible_groups.values())
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Groups as Admin", admin_count)
                    with col2:
                        st.metric("Groups as Member", member_count)
                    with col3:
                        st.metric("Total Team Members", total_members)
    
    with tab2:
        # ALL GROUPS VIEW - List of all groups with access status
        st.subheader("🌐 All Groups in System")
        st.caption("View all groups and your access status")
        
        all_groups = get_all_groups_for_display()
        
        if not all_groups:
            st.info("No groups have been created yet. Create one in the 'My Groups' tab!")
        else:
            # Create a nice display
            for group_info in all_groups:
                with st.container():
                    col1, col2 = st.columns([4, 1])
                    
                    with col1:
                        st.markdown(f"### {group_info['name']}")
                        st.caption(f"👤 Admin: {group_info['admin_name']} ({group_info['admin_email']})")
                        st.caption(f"👥 Members: {group_info['member_count']} | 📅 Created: {datetime.fromisoformat(group_info['created_at']).strftime('%Y-%m-%d')}")
                    
                    with col2:
                        if group_info['is_admin']:
                            st.success("👑 Admin")
                        elif group_info['has_access']:
                            st.info("✅ Member")
                        else:
                            st.warning("🔒 No Access")
                    
                    if not group_info['has_access']:
                        st.caption("💡 You need to be added by the group admin to access this group")
                    
                    st.markdown("---")
    
    # Footer
    st.markdown("---")
    st.caption("💡 All data is automatically saved and persists between sessions")
    st.caption("🔒 You can only access groups where you are admin or have been added as a member")
    st.caption(f"📁 Storage files: {STORAGE_FILE.absolute()} | {USERS_FILE.absolute()}")