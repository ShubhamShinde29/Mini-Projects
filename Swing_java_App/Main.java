
import javax.swing.*;
import java.awt.*;
public class Main {
	
	public void Login() {
		
		JFrame frame=new JFrame("Registration Form");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setSize(600, 400);
		
		JPanel panel=new JPanel();
		JLabel label1=new JLabel("Username ");
		label1.setHorizontalTextPosition(JLabel.LEFT);
		label1.setVerticalTextPosition(JLabel.CENTER);

		JTextField jt1=new JTextField(20);
		JLabel label2=new JLabel("Password ");
		label2.setHorizontalTextPosition(JLabel.LEFT);

		JTextField jt2=new JTextField(20);

		JButton Login=new JButton("Login");
		
		panel.add(label1);
		panel.add(jt1);
		panel.add(label2);
		panel.add(jt2);
		panel.add(Login);
		
		frame.getContentPane().add(BorderLayout.CENTER, panel);
		
		frame.setVisible(true);
		
	}
	
	public static void main(String[] args) {
		
		Main m=new Main();
		m.Login();
	}

}
