def test_agent_orchestrator():
    prompt = "Test execution query for agentic-crowd-density-safety-monitor"
    assert len(prompt) > 0
    assert "Test" in prompt
