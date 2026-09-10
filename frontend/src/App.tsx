import React, { useState } from 'react';

export default function App() {
  const [prompt, setPrompt] = useState('');
  const [res, setRes] = useState<any>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const response = await fetch('http://localhost:8000/api/v1/agent/run', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt })
    });
    const data = await response.json();
    setRes(data);
  };

  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif', maxWidth: '800px', margin: '0 auto' }}>
      <h1>Agentic Public Crowd Density & Safety Monitor</h1>
      <p>Multi-agent event crowd monitoring, bottleneck detector, and security dispatch alert agent.</p>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={prompt}
          onChange={e => setPrompt(e.target.value)}
          placeholder="Enter agent query..."
          style={{ width: '100%', padding: '0.75rem', borderRadius: '6px', border: '1px solid #ccc' }}
        />
        <button type="submit" style={{ marginTop: '1rem', padding: '0.75rem 1.5rem', background: '#0d9488', color: '#fff', border: 'none', borderRadius: '6px' }}>
          Run Agent
        </button>
      </form>
      {res && <pre style={{ marginTop: '1.5rem', background: '#f8fafc', padding: '1rem', borderRadius: '6px' }}>{JSON.stringify(res, null, 2)}</pre>}
    </div>
  );
}
