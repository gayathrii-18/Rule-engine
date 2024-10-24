from flask import Flask, request, jsonify, render_template
from app.api import create_rule, combine_rules, evaluate_rule
from app.database import init_db, save_rule, get_rule

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_rule', methods=['POST'])
def api_create_rule():
    rule_string = request.json['rule']
    name = request.json['name']
    ast = create_rule(rule_string)
    save_rule(name, ast)
    return jsonify(ast.to_dict())

@app.route('/combine_rules', methods=['POST'])
def api_combine_rules():
    rule_names = request.json['rules']
    rules = [get_rule(name).to_dict() for name in rule_names]
    combined_ast = combine_rules([json.dumps(rule) for rule in rules])
    return jsonify(combined_ast.to_dict())

@app.route('/evaluate_rule', methods=['POST'])
def api_evaluate_rule():
    rule_json = request.json['rule']
    data = request.json['data']
    result = evaluate_rule(rule_json, data)
    return jsonify({"result": result})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
