import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import JumboTron from 'react-bootstrap/JumboTron';
import './App.css';

function App() {
  return (
    <div className="App">
      <JumboTron background-color='red'>
        Hello! Thank you for using <strong>W8R</strong>. Please input your phone number and order number below.
      </JumboTron>

      <div class='container'>
        <Form>
          <Form.Group controlId="orderNumber">
            <Form.Label>Order Number</Form.Label>
            <Form.Control size='lg' type="text" placeholder="Enter Order Number" />
            <Form.Text className="text-muted">
              Put your order number here so we know to deliver you the right stuff!
            </Form.Text>
          </Form.Group>

          <Form.Group controlId="phoneNumber">
            <Form.Label>Phone Number</Form.Label>
            <Form.Control  size='lg' type="text" placeholder="Enter Phone Number" />
            <Form.Text className="text-muted">
              We use text messages to allow you to partially control our bots and let you know when food is coming.
            </Form.Text>
          </Form.Group>

          <Button size='lg' variant="primary" type="submit">
            Submit
          </Button>
        </Form>
      </div>
    </div>
  );
}

export default App;
