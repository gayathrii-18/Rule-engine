async function createRule() {
    const name = document.getElementById('ruleName').value;
    const rule = document.getElementById('ruleInput').value;
    const response = await fetch('/create_rule', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, rule })
    });
    const result = await response.json();
    document.getElementById('ruleOutput').textContent = JSON.stringify(result, null, 2);
}

async function combineRules() {
    const rules = document.getElementById('rulesInput').value.split('\n');
    const response = await fetch('/combine_rules', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ rules })
    });
    const result = await response.json();
    document.getElementById('combinedOutput').textContent = JSON.stringify(result, null, 2);
}

async function evaluateRule() {
    const rule = JSON.parse(document.getElementById('ruleJsonInput').value);
    const data = JSON.parse(document.getElementById('dataInput').value);
    const response = await fetch('/evaluate_rule', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ rule, data })
    });
    const result = await response.json();
    document.getElementById('evaluationOutput').textContent = JSON.stringify(result, null, 2);
}

document.getElementById('createRuleBtn').addEventListener('click', createRule);
document.getElementById('combineRulesBtn').addEventListener('click', combineRules);
document.getElementById('evaluateRuleBtn').addEventListener('click', evaluateRule);
