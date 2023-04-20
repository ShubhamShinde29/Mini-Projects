package demo;

import java.awt.*;
import javax.swing.*;

import javax.swing.border.EmptyBorder;
import java.awt.event.*;
import java.sql.Connection;
import java.sql.PreparedStatement;

public class SignUp extends JFrame {

    private static final long serialVersionUID = 1L;
    private JTextField textField;
    private JPasswordField passwordField;
    private JButton btnNewButton, btnNewButton1;
    private JLabel label;
    private JPanel contentPane;

    public static void main(String[] args) {
        EventQueue.invokeLater(new Runnable() {
            public void run() {
                try {
                    SignUp frame = new SignUp();
                    frame.setVisible(true);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });
    }

    public SignUp() {

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setBounds(450, 190, 1070, 500);
        setResizable(false);

        contentPane = new JPanel();
        contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
        setContentPane(contentPane);
        contentPane.setLayout(null);

        JLabel lblNewLabel = new JLabel("Student Registration Form");
        lblNewLabel.setForeground(Color.BLACK);
        lblNewLabel.setFont(new Font("Times New Roman", Font.PLAIN, 35));
        lblNewLabel.setBounds(350, 5, 400, 93);
        contentPane.add(lblNewLabel);

        JLabel lblUsername = new JLabel("Username");
        lblUsername.setBackground(Color.BLACK);
        lblUsername.setForeground(Color.BLACK);
        lblUsername.setFont(new Font("Tahoma", Font.PLAIN, 25));
        lblUsername.setBounds(150, 100, 150, 32);
        contentPane.add(lblUsername);

        JLabel lblPassword = new JLabel("Password");
        lblPassword.setForeground(Color.BLACK);
        lblPassword.setBackground(Color.CYAN);
        lblPassword.setFont(new Font("Tahoma", Font.PLAIN, 25));
        lblPassword.setBounds(600, 100, 150, 32);
        contentPane.add(lblPassword);

        JLabel name = new JLabel("Enter Name");
        name.setBackground(Color.BLACK);
        name.setForeground(Color.BLACK);
        name.setFont(new Font("Tahoma", Font.PLAIN, 25));
        name.setBounds(150, 200, 150, 32);
        contentPane.add(name);

        JLabel Mob = new JLabel("Mobile No");
        Mob.setBackground(Color.BLACK);
        Mob.setForeground(Color.BLACK);
        Mob.setFont(new Font("Tahoma", Font.PLAIN, 25));
        Mob.setBounds(600, 200, 150, 32);
        contentPane.add(Mob);

        JLabel course = new JLabel("Course");
        course.setBackground(Color.BLACK);
        course.setForeground(Color.BLACK);
        course.setFont(new Font("Tahoma", Font.PLAIN, 25));
        course.setBounds(150, 300, 150, 32);
        contentPane.add(course);

        JLabel c = new JLabel("Class");
        c.setBackground(Color.BLACK);
        c.setForeground(Color.BLACK);
        c.setFont(new Font("Tahoma", Font.PLAIN, 25));
        c.setBounds(600, 300, 150, 32);
        contentPane.add(c);

        textField = new JTextField();
        textField.setFont(new Font("Tahoma", Font.PLAIN, 35));
        textField.setBounds(300, 100, 181, 35);
        contentPane.add(textField);
        textField.setColumns(10);

        passwordField = new JPasswordField();
        passwordField.setFont(new Font("Tahoma", Font.PLAIN, 35));
        passwordField.setBounds(750, 100, 181, 35);
        contentPane.add(passwordField);

        textField = new JTextField();
        textField.setFont(new Font("Tahoma", Font.PLAIN, 32));
        textField.setBounds(300, 200, 181, 35);
        contentPane.add(textField);
        textField.setColumns(10);

        textField = new JTextField();
        textField.setFont(new Font("Tahoma", Font.PLAIN, 32));
        textField.setBounds(750, 200, 181, 35);
        contentPane.add(textField);
        textField.setColumns(10);

        textField = new JTextField();
        textField.setFont(new Font("Tahoma", Font.PLAIN, 32));
        textField.setBounds(300, 300, 181, 35);
        contentPane.add(textField);
        textField.setColumns(10);

        textField = new JTextField();
        textField.setFont(new Font("Tahoma", Font.PLAIN, 32));
        textField.setBounds(750, 300, 181, 35);
        contentPane.add(textField);
        textField.setColumns(10);

        btnNewButton = new JButton("Submit");
        btnNewButton.setFont(new Font("Tahoma", Font.PLAIN, 26));
        btnNewButton.setBounds(450, 392, 200, 50);

    /*    btnNewButton.addActionListener(new ActionListener() {

            public void actionPerformed(ActionEvent e) {
                String userName = textField.getText();
                String Password = passwordField.getText();
                String Enter_Name = textField.getText();
                String Mobile_No = textField.getText();
                String course = textField.getText();
                String c = textField.getText();
                int flag = 0;
                Class.forName("com.mysql.jdbc.Driver");
                Connection connection = (Connection) DriverManager.getConnection("jdbc:mysql://localhost:3306/activity",
                        "root", "root");
                PreparedStatement st, st1;
                try {
                    st = (PreparedStatement) connection
                            .prepareStatement("Select username from student where username=? ");
			  st.setString(1,userName);
                    ResultSet rs = st.executeQuery();
                    if(rs.next()) {
                            flag = 1;
                            break;
                        }
                    }
                    connection.close();

                    if (flag == 0) {
                        dispose();
                        st1 = connection.prepareStatement(
                                "insert into student(username,pass,name,mob,course,class)values(?,?,?,?,?,?)");
                        st1.setString(1, userName);
                        st1.setString(2, Password);
                        st1.setString(3, Enter_Name);
                        st1.setString(4, Mobile_No);
                        st1.setString(5, course);
                        st1.setString(4, c);
                        st1.executeUpdate();
                        connection.close();
                        JOptionPane.showMessageDialog(btnNewButton, "Your form is successfully Submitted");
                    } else {
                        JOptionPane.showMessageDialog(btnNewButton, "Username already taken ..Enter again ");
                    }
                } catch (SQLException sqlException) {
                    sqlException.printStackTrace();
                }
            }
        });
	*/
        contentPane.add(btnNewButton);
    }

}
