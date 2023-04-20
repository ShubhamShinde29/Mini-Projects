package demo;

import java.awt.*;
import javax.swing.*;
import java.sql.*;
	
public class SqlConnection extends JFrame {

	 

	public void check(String userName,String password,JButton btnNewButton) throws ClassNotFoundException {

		PreparedStatement st,st1;
		Connection connection,con;
          	try {
				Class.forName("com.mysql.jdbc.Driver");
          		connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/activity","root", "root");
          
          		st = connection.prepareStatement("Select username, pass from student where username=? and pass=?");
          		st.setString(1, userName);
          		st.setString(2, password);
				ResultSet rs = st.executeQuery();

          		con = (Connection)DriverManager.getConnection("jdbc:mysql://localhost:3306/activity","root", "root");
				st1=con.prepareStatement("Select admin_username, password from admin where admin_username=? and password=?");
				st1.setString(1, userName);
          		st1.setString(2, password);
				AdminHome a = new AdminHome(userName);
				UserHome ah = new UserHome(userName);

          		ResultSet rs1 = st1.executeQuery();
          		if (rs1.next()) {
          			dispose();
          			
          			a.setTitle("Welcome "+userName);
          			a.setVisible(true);
          			JOptionPane.showMessageDialog(btnNewButton,"You have successfully logged in");
          		}else if(rs.next()) {
					dispose();
					
          			ah.setTitle("Welcome "+userName);
          			ah.setVisible(true);
          			JOptionPane.showMessageDialog(btnNewButton,"You have successfully logged in");
				}else {
          			JOptionPane.showMessageDialog(btnNewButton, "Wrong Username & Password");
          		}
				connection.close();
          	} catch (SQLException sqlException) {
          		sqlException.printStackTrace();
          	}

    }
}