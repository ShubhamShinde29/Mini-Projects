package demo;

import java.awt.event.*;
import java.awt.*;
import javax.swing.*;
import javax.swing.border.EmptyBorder;

public class UserHome extends JFrame {

    private static final long serialVersionUID = 1L;
    private JPanel contentPane;

    /**
     * Launch the application.
     */
    public static void main(String[] args) {
        EventQueue.invokeLater(new Runnable() {
            public void run() {
                try {
                    UserHome frame = new UserHome();
                    frame.setVisible(true);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });
    }

	public UserHome(){

	}
    	public UserHome(String s){
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        	setBounds(450, 190, 1014, 597);
        	setResizable(false);
		contentPane = new JPanel();
        	contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
        	setContentPane(contentPane);
 	 	contentPane.setLayout(null);
	}
	

}