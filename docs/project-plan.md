# DevSentry Project Plan

## Phase 0 — Requirements and Design
- [x] Define project name
- [x] Define problem statement
- [x] Define target users and use cases
- [x] Define architecture
- [x] Define technology stack
- [x] Define security boundaries
- [x] Define MVP scope
- [x] Create GitHub repository
- [x] Initialize local Git repository
- [ ] Complete Phase 0 checkpoint

## Phase 1 — Development Environment
- [ ] Verify Git Bash
- [ ] Verify Git
- [ ] Verify Python
- [ ] Verify AWS CLI
- [ ] Create Python virtual environment
- [ ] Create environment configuration
- [ ] Establish secret-handling rules
- [ ] Complete reproducible local environment

## Phase 2 — Basic AI Chat MVP
- [ ] Create FastAPI backend
- [ ] Create chat API
- [ ] Create web chat interface
- [ ] Connect LLM
- [ ] Implement responses
- [ ] Test local chat

## Phase 3 — Conversation Memory
- [ ] Create conversation/session model
- [ ] Store recent messages
- [ ] Add conversation IDs
- [ ] Manage context window
- [ ] Add persistence interface

## Phase 4 — Log Ingestion
- [ ] Collect sample logs
- [ ] Normalize logs
- [ ] Add timestamps and metadata
- [ ] Store selected logs in S3
- [ ] Create log retrieval functions

## Phase 5 — RAG
- [ ] Prepare documents/log summaries
- [ ] Chunk data
- [ ] Create retrieval/index layer
- [ ] Retrieve relevant evidence
- [ ] Assemble AI context
- [ ] Add source references

## Phase 6 — DevOps Tool Calling
- [ ] Define tool schemas
- [ ] Implement read-only tools
- [ ] Validate tool inputs
- [ ] Add timeouts
- [ ] Test tool execution

## Phase 7 — Incident Analysis
- [ ] Detect symptoms
- [ ] Build event timeline
- [ ] Correlate evidence
- [ ] Identify root-cause hypotheses
- [ ] Separate evidence from hypotheses
- [ ] Generate recommendations
- [ ] Generate incident reports

## Phase 8 — AWS Deployment
- [ ] Create EC2
- [ ] Configure Ubuntu
- [ ] Deploy FastAPI backend
- [ ] Create S3 bucket
- [ ] Deploy frontend to S3
- [ ] Configure CloudFront
- [ ] Configure secure connectivity
- [ ] Configure secrets safely

## Phase 9 — Git Bash Automation
- [ ] setup.sh
- [ ] deploy.sh
- [ ] deploy-frontend.sh
- [ ] deploy-backend.sh
- [ ] collect-logs.sh
- [ ] health-check.sh
- [ ] Add AWS CLI automation
- [ ] Add deployment verification

## Phase 10 — Security and Reliability
- [ ] Least-privilege IAM
- [ ] Secure API endpoints
- [ ] Validate tool inputs
- [ ] Command allowlists
- [ ] Timeouts
- [ ] Rate limits
- [ ] Log sanitization
- [ ] Error handling
- [ ] Backups

## Phase 11 — Monitoring
- [ ] Health endpoint
- [ ] Structured logs
- [ ] Application metrics
- [ ] Tool execution metrics
- [ ] Latency tracking
- [ ] Basic alerts

## Phase 12 — Testing and Demonstration
- [ ] 502 investigation
- [ ] Failed deployment
- [ ] Backend stopped
- [ ] High disk usage
- [ ] Memory/resource issue
- [ ] Configuration issue
- [ ] RAG question
- [ ] Multi-turn troubleshooting
- [ ] Security tests
- [ ] Rollback test

## Phase 13 — Documentation and Portfolio
- [ ] Architecture diagram
- [ ] README
- [ ] Installation guide
- [ ] AWS deployment guide
- [ ] API documentation
- [ ] Security documentation
- [ ] Demo screenshots
- [ ] Troubleshooting examples
- [ ] Final report
- [ ] Presentation/demo script
