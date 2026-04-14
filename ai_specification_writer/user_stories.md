# User Stories

### User Story 1
As a corporate employee, I want to find colleagues with similar commute routes and schedules so that I can share rides, reduce costs, and build workplace relationships.

**Acceptance Criteria**:
- User enters home address and work arrival/departure times.
- System matches employees within a 2-mile radius of the user's route.
- Schedule flexibility of ±30 minutes is considered in matching.
- At least 3 match options are displayed with compatibility scores.
- Matches update automatically when schedules change.

**Priority**: MVP


### User Story 2
As a corporate employee, I want to communicate with my carpool group inside the app so that I can coordinate pickups and handle schedule changes without switching platforms.

**Acceptance Criteria**:
- In-app group messaging is available for each active carpool.
- Users receive push notifications for new messages and schedule changes.
- Calendar events are automatically updated when trip details change.
- Emergency contact information is accessible within the carpool group view.

**Priority**: MVP


### User Story 3
As an IT administrator, I want to integrate CarpoolConnect with our corporate identity provider so that employees can log in with their existing credentials without a separate account.

**Acceptance Criteria**:
- SSO is supported for Active Directory, Okta, and Azure AD.
- Users are automatically provisioned on first login.
- Deprovisioning removes access within 24 hours of HR system update.
- Role-based access control is enforced based on corporate directory groups.
- Integration passes corporate security policy compliance review.

**Priority**: MVP


### User Story 4
As a sustainability officer, I want to view real-time CO2 savings from carpooling activity so that I can measure and report progress toward our corporate environmental goals.

**Acceptance Criteria**:
- CO2 savings are calculated and displayed per trip, per user, and company-wide.
- Monthly and annual sustainability reports can be exported in PDF and CSV formats.
- Reports include benchmarking data against industry standards.
- Dashboard is accessible to sustainability officers via role-based permissions.

**Priority**: High


### User Story 5
As an HR manager, I want to see individual and aggregate cost savings from carpooling so that I can demonstrate the ROI of the program to company leadership.

**Acceptance Criteria**:
- Dashboard shows per-employee savings compared to solo driving and parking costs.
- Aggregate savings are summarized at team, department, and company levels.
- ROI analysis report can be generated and exported for executive review.
- Employee satisfaction scores from carpool participants are collected and displayed.

**Priority**: High


### User Story 6
As a facility manager, I want to allocate reserved parking spots to carpoolers so that I can reduce parking congestion and reward program participation.

**Acceptance Criteria**:
- Carpoolers with active trips receive reserved spot assignments automatically.
- Parking availability is updated in real-time and visible to eligible users.
- Integration with existing parking management systems is supported via REST API.
- Analytics report shows before/after parking utilization improvements.

**Priority**: High


### User Story 7
As a corporate employee, I want to view my personal commute history and savings so that I can track my individual contribution to cost reduction and sustainability.

**Acceptance Criteria**:
- Profile page displays total trips taken, kilometers shared, CO2 saved, and money saved.
- Data is available for the current month, quarter, and year.
- Employee can download a personal impact summary report.
- Stats are updated within 1 hour of a completed trip.

**Priority**: Medium

### User Story 8
As a C-suite executive, I want to access a high-level dashboard of carpooling program performance so that I can monitor its contribution to corporate sustainability and cost reduction targets.

**Acceptance Criteria**:
- Executive dashboard displays KPIs: participation rate, CO2 savings, cost savings, and retention impact.
- Data can be visualized in integrated tools such as Tableau or Power BI.
- Dashboard is accessible via single sign-on with no additional credentials.
- Reports can be scheduled for automatic delivery to stakeholder email lists.

**Priority**: Medium


