import webapp2

html_form = """
<!DOCTYPE html>
<html>
<head>
    <title>Calculator</title>
</head>
<body>
    <h1>Calculator</h1>
    <form action="/" method="post">
        <label for="num1">Number 1:</label>
        <input type="number" id="num1" name="num1" required><br><br>
        <label for="num2">Number 2:</label>
        <input type="number" id="num2" name="num2" required><br><br>
        <label for="operation">Operation:</label>
        <select id="operation" name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select><br><br>
        <input type="submit" value="Calculate">
    </form>
</body>
</html>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(html_form)
    
    def post(self):
        try:
            num1 = float(self.request.get('num1'))
            num2 = float(self.request.get('num2'))
            operation = self.request.get('operation')
            
            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 == 0:
                    result = "Error! Division by zero."
                else:
                    result = num1 / num2
            else:
                result = "Invalid operation"
            
            self.response.write(html_form)
            self.response.write("<h2>Result: {}</h2>".format(result))
        except ValueError:
            self.response.write(html_form)
            self.response.write("<h2>Error! Invalid input.</h2>")

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)