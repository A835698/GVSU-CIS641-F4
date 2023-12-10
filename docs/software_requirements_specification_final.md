# Overview
This document outlines the software requirements for the "Optimized Team Maker" system. It covers both functional and non-functional requirements to provide a comprehensive understanding of the project's scope and features.

# Software Requirements

## Functional Requirements

### Admin Authentication
| ID  | Requirement |
|:---:|:-----------:|
| FR1 | The system should allow Admins to log in. |
| FR2 | Admins must use unique usernames. |
| FR3 | Passwords must be securely stored and hashed. |
| FR4 | Failed login attempts should trigger account lockout. |
| FR5 | Admins should be able to reset their passwords. |

### Team Creation and Management
| ID  | Requirement |
|:---:|:-----------:|
| FR6 | Teams must be linked to a specific project. |
| FR7 | Each team must have a unique name within a project. |
| FR8 | Add or remove team members. |
| FR9 | The system should support the creation of multiple teams per project. |
| FR10 | Teams can be disbanded after project completion. |

### Skill Analysis and Matching
| ID   | Requirement |
|:----:|:-----------:|
| FR11 | The system must analyze the skills of each team member. |
| FR12 | Skills should be categorized based on proficiency levels. |
| FR13 | Teams should be automatically matched based on required skills. |
| FR14 | Matching algorithm should prioritize skill diversity within teams. |
| FR15 | Skill analysis should be performed periodically. |

### Project Organization
| ID   | Requirement |
|:----:|:-----------:|
| FR16 | Projects must have a unique name. |
| FR17 | Teams should be organized under specific projects. |
| FR18 | Project managers should view all teams in their projects. |
| FR19 | Projects can be archived or closed. |
| FR20 | Teams cannot be created without associating them with a project. |

### Reporting and Analytics
| ID   | Requirement |
|:----:|:-----------:|
| FR21 | The system should generate reports on team performance. |
| FR22 | Project managers receive notifications for important team events. |
| FR23 | Analytics provide insights into skill utilization. |
| FR24 | Reports should be exportable in common formats (e.g., PDF, CSV). |
| FR25 | Accessible team efficiency metrics. |

### User Notifications
| ID   | Requirement |
|:----:|:-----------:|
| FR26 | Users receive notifications for team events. |
| FR27 | Team members notified of additions or removals. |
| FR28 | Project managers alerted for critical team issues. |
| FR29 | Customizable notification preferences. |
| FR30 | Notifications support various channels. |

### Team Communication
| ID   | Requirement |
|:----:|:-----------:|
| FR31 | Teams should have a built-in chat/messaging feature. |
| FR32 | Searchable team chat messages. |
| FR33 | Support file attachments in team messages. |
| FR34 | Team members receive chat message notifications. |
| FR35 | Archive team chat history. |

## Non-Functional Requirements

### Performance
| ID   | Requirement |
|:----:|:-----------:|
| NFR1 | The system must load within 3 seconds. |
| NFR2 | Team operations complete within 5 seconds. |
| NFR3 | Handles at least 100 concurrent users. |
| NFR4 | Real-time skill analysis. |
| NFR5 | Reports generated within 10 seconds. |

### Security
| ID   | Requirement |
|:----:|:-----------:|
| NFR6 | User passwords securely stored. |
| NFR7 | The system should implement role-based access control. |
| NFR8 | Data transmission encrypted using HTTPS. |
| NFR9 | Mechanisms to detect and prevent common security threats. |
| NFR10 | Log and monitor user activities. |

### Reliability
| ID   | Requirement |
|:----:|:-----------:|
| NFR11 | The system should have an uptime of at least 99%. |
| NFR12 | Daily data backups. |
| NFR13 | Recoverable team data after system failures. |
| NFR14 | Helpful error messages. |
| NFR15 | Mechanism for detecting and handling unexpected errors. |

### Usability
| ID   | Requirement |
|:----:|:-----------:|
| NFR16 | Intuitive and user-friendly interface. |
| NFR17 | Tooltips and help sections for users. |
| NFR18 | Users perform common tasks with minimal training. |
| NFR19 | Accessible to users with disabilities. |
| NFR20 | Support for multiple languages. |

### Scalability
| ID   | Requirement |
|:----:|:-----------:|
| NFR21 | System scales for growing projects and teams. |
| NFR22 | Database handles increasing data volume. |
| NFR23 | Performance does not degrade with increased load. |
| NFR24 | Supports a growing number of concurrent users. |
| NFR25 | Easily integrates new features and modules for scalability. |

### Responsiveness
| ID   | Requirement |
|:----:|:-----------:|
| NFR26 | Responsive design for desktop, tablet, and mobile. |
| NFR27 | Optimized page load times. |
| NFR28 | UI elements adapt to different screen sizes. |
| NFR29 | Performance testing for responsiveness under varying network conditions. |
| NFR30 | Support offline access for certain functionalities. |

### Accessibility
| ID   | Requirement |
|:----:|:-----------:|
| NFR31 | UI complies with WCAG accessibility standards. |
| NFR32 | Accessibility features support screen readers and keyboard navigation. |
| NFR33 | Regular accessibility audits and improvements. |
| NFR34 | Provide alternative text for images and multimedia elements. |
| NFR35 | Usability testing with users of diverse abilities. |

# Integration Plan

## Training Approach:
To facilitate a smooth transition, a comprehensive training program will be initiated. This program will include user-friendly tutorials, hands-on workshops, and personalized assistance. The training will be tailored to cater to different learning styles and skill levels, ensuring that all users, from novice to experienced engineers, feel comfortable and competent using the application.

## Ecosystem Integration:
The application's seamless integration into the existing corporate ecosystem is a priority. A dedicated integration team will collaborate closely with the customer's IT department to understand their infrastructure, software dependencies, and security protocols. Customization options will be explored to adapt the application to specific workflows, ensuring minimal disruption and maximum compatibility.

## Issue Resolution Protocol:
A robust issue resolution protocol will be established to promptly address any concerns. A user-friendly interface within the application will allow users to report issues efficiently. A dedicated support team will triage and prioritize reported issues, ensuring a swift resolution process. Regular updates, bug fixes, and feature enhancements will be rolled out to enhance user experience and address evolving needs. Additionally, periodic check-ins and feedback sessions will be conducted to proactively identify and resolve potential issues.


# Use Case Diagrams

| Artifact                  | Linked Requirements                  |
| ------------------------- | ------------------------------------ |
| Team Creation Use Case    | UC1: Create Team                     |
| Join Team Use Case        | UC2: Join Team                       |
| Browse Teams Use Case     | UC3: Browse Teams                    |
| View Team Details Use Case| UC4: View Team Details               |
| Generate Teams Use Case   | UC5: Generate Teams                  |
| User Authentication Use Case | UC6: User Authentication          |

# Class Diagrams

| Artifact                  | Linked Requirements                  |
| ------------------------- | ------------------------------------ |
| User Class                | FR1: Admin Authentication            |
| TeamMember Class          | FR8: Team Members can be added/removed |
| Skill Class               | FR13: Skills should be categorized   |
| Team Class                | FR6: Teams must be associated with a project |
| Project Class             | FR16: Projects must have a unique name |
| TeamMaker Class           | FR26: Notifications for upcoming team events |
|                           | FR31: Teams should have a built-in chat/messaging feature |

# Activity Diagrams

| Artifact                  | Linked Requirements                  |
| ------------------------- | ------------------------------------ |
| Team Creation Activity    | FR6: Teams must be associated with a project |
| Join Team Activity        | FR7: Each team must have a unique name |
| Browse Teams Activity     | FR18: Project managers should be able to view all teams |
| View Team Details Activity| FR8: Team members can be added/removed |
| Generate Teams Activity   | FR13: Teams should be automatically matched based on required skills |
| User Authentication Activity | FR1: Admin Authentication          |
|                           | FR29: Notification preferences should be customizable |

# Artifacts Repository

You can find all the use case diagrams, class diagrams, and object diagrams in the [Artifacts](https://github.com/A835698/GVSU-CIS641-F4/tree/master/artifacts) repository. Explore the provided path to access detailed visual representations of the project's architecture and design.




## Additional Note:
Future implemented requirements are referred from Google and AI prompting.
