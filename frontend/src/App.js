import React from 'react';
import './App.css';
import axios from "axios";

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.withCredentials = true;

class App extends React.Component {
	constructor(props) {
		super(props);

		this.state = {
			"data": null
		}
	}

	componentDidMount() {
		if (!this.state.data) {
			axios.get('/request/', {}).then(result => {
				this.setState({data: result.data})
			});
		}
	}

	render() {
		return (
			<div className="App">

				{this.state.data ? this.state.data.map((value) => {
					return <div key={value.id}>{value.type}, {value.text}</div>
				}) : null}

			</div>
		);
	}
}

export default App;
