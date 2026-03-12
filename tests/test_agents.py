from tensoredge.agents import EdgeAgent

def test_agent_initialization():
    agent = EdgeAgent(model_path="dummy.tedge", role="tester")
    assert agent.role == "tester"
    assert len(agent.context) == 0

def test_agent_processing():
    agent = EdgeAgent(model_path="dummy.tedge", role="tester", threshold=0.0)
    result = agent.process({"input": 1})
    assert "Action Triggered" in result
