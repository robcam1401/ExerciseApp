import 'dart:io';
import 'dart:convert';

void main() {
	print('Hello, World!');
	const insert_data = {
		'Action' : 'I',
		'Function' : 'new_user',
		'AccountNumber' : 4, 
		'Username' : 'Test1',
		'PasswordHash' : 'ABCD',
		'Email' : '123@abc.net',
		'PhoneNumber' : 3,
		'Fname' : 'Test',
		'Minit' : 'T',
		'Lname' : '2',
		'UserDoB' : '1111-11-11 11:11:11'
		};
	const query_data = {
		'Action' : 'Q',
		'Function' : 'account_info',
		'AccountNumber' : 4
		};
	final String query_json = jsonEncode(query_data);
	print(query_json);
    connect_to_server(query_json);
    }

void connect_to_server(send_string) async {
  // Define the server's IP address and port
    final String serverIp = 'localhost'; // Change to the server's IP address
    final int serverPort = 12000; // Change to the server's port

    try {
    // Create a socket connection to the server
		final socket = await Socket.connect(serverIp, serverPort);

		// Send data to the server
		socket.writeln(send_string);

		// Listen for data from the server
		socket.listen(
			(data) {
				print('Received from server: ${String.fromCharCodes(data)}');
			},
			onDone: () {
				print('Server disconnected.');
				socket.destroy();
			},
			onError: (error) {
				print('Error: $error');
				socket.destroy();
			},
		);

		// Close the socket when you're done
		socket.close();
	} 
	catch (e) {
    	print('Error: $e');
  	}
}

