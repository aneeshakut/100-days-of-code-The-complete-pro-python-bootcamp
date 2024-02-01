import turtle

def draw_rectangle(x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)

def draw_text(x, y, text):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(text, font=("Arial", 12, "normal"))

def mail_merge(data):
    for record in data:
        draw_rectangle(0, 0, 200, 100)
        draw_text(20, 70, f"Name: {record['name']}")
        draw_text(20, 50, f"Address: {record['address']}")
        draw_text(20, 30, f"City: {record['city']}")
        draw_text(20, 10, f"State: {record['state']}")
        turtle.penup()
        turtle.goto(0, 0)
        turtle.clear()

if __name__ == "__main__":
    turtle.speed(1)
    
    data = [
        {"name": "John Doe", "address": "123 Main St", "city": "Cityville", "state": "CA"},
        {"name": "Jane Smith", "address": "456 Oak St", "city": "Townsville", "state": "NY"},
        # Add more records as needed
    ]

    mail_merge(data)
    turtle.done()
