import os, sys ,time
from PySide import QtGui, QtCore 
import paramiko
from ciscoconfparse import CiscoConfParse
class MainWindow(QtGui.QWidget): 
    def __init__(self): 
        QtGui.QWidget.__init__(self) 
        self.setGeometry(100,100, 700,650) 
        self.setWindowTitle("Cross-platform Routing Application") 
        self.setWindowIcon(QtGui.QIcon("map.jpg")) 
        self.setToolTip("Cross-platform Routing Application")
        self.resize(700,650) 
        self.setMinimumSize(700,650) 
        #start of first section tab-----------------------------------------------------------------------------------------------
        section1 = QtGui.QTabWidget()			#object of first section tab
#print(section1.currentIndex())
        cisco = QtGui.QWidget()					#widget of first section tab 
        linux = QtGui.QWidget()					#widget of first section tab 
        about = QtGui.QWidget()
        global about_layout					#widget of first section tab 
        cisco_layout = QtGui.QFormLayout(cisco)			#layout of first section tab  
        linux_layout = QtGui.QFormLayout(linux)			#layout of first section tab  
        about_layout = QtGui.QFormLayout(about) 		#layout of first section tab 
        section1.addTab(cisco, "Cisco") 		#section1 tab1
        section1.addTab(linux, "Linux")			#section1 tab2
        section1.addTab(about, "About")			#section1 tab3
        #end of first section tab-----------------------------------------------------------------------------------------------
        
#----------------------------------------------cisco section2 tab--------------------------------------------------------------#
        section2 = QtGui.QTabWidget()			#object of seond section tab
        connection = QtGui.QWidget()			#widget of second section tab
        add_configuration = QtGui.QWidget()		#widget of second section tab
        remove_configuration = QtGui.QWidget()	
        view_info = QtGui.QWidget()				#widget of second section tab
        global connection_layout
        connection_layout = QtGui.QFormLayout(connection)
        add_configuration_layout = QtGui.QFormLayout(add_configuration)
        remove_configuration_layout = QtGui.QFormLayout(remove_configuration)
        view_info_layout = QtGui.QFormLayout(view_info)
        section2.addTab(connection,"Connection")
        section2.addTab(add_configuration,"Add Configuration")
        section2.addTab(remove_configuration,"Rrmove Configuration")
        section2.addTab(view_info,"View Infromation")
        cisco_layout.addWidget(section2) #add section2 to cisco tab
#----------------------------------------------cisco section2 tab--------------------------------------------------------#
#----------------------------------------------linux section2 tab---------------------------------------------------------#
        linux_section2 = QtGui.QTabWidget()			#object of seond section tab
        global linux_connection_layout
        linux_connection = QtGui.QWidget()			#widget of second section tab
        linux_add_configuration = QtGui.QWidget()		#widget of second section tab
        linux_remove_configuration = QtGui.QWidget()	
        linux_view_info = QtGui.QWidget()				#widget of second section tab
        linux_connection_layout = QtGui.QFormLayout(linux_connection)
        linux_add_configuration_layout = QtGui.QFormLayout(linux_add_configuration)
        linux_remove_configuration_layout = QtGui.QFormLayout(linux_remove_configuration)
        linux_view_info_layout = QtGui.QFormLayout(linux_view_info)
        linux_section2.addTab(linux_connection,"Connection")
        linux_section2.addTab(linux_add_configuration,"Add Configuration")
        linux_section2.addTab(linux_remove_configuration,"Rrmove Configuration")
        linux_section2.addTab(linux_view_info,"View Infromation")
        linux_layout.addWidget(linux_section2) #add section2 to cisco tab
#----------------------------------------------linux section2 tab---------------------------------------------------------------#

#----------------------------------add_configuratin section tab----------------------------------------------------------#
        add_config_section = QtGui.QTabWidget()
        global static_tab_layout
        global rip_tab_layout
        global ospf_tab_layout
        static_tab = QtGui.QWidget()
        rip_tab = QtGui.QWidget()	
        ospf_tab = QtGui.QWidget()
        eigrp_tab = QtGui.QWidget()	
        static_tab_layout = QtGui.QFormLayout(static_tab)
        rip_tab_layout = QtGui.QFormLayout(rip_tab)
        ospf_tab_layout = QtGui.QFormLayout(ospf_tab)
        eigrp_tab_layout = QtGui.QFormLayout(eigrp_tab)
        add_config_section.addTab(static_tab,"Static")
        add_config_section.addTab(rip_tab,"Rip")
        add_config_section.addTab(ospf_tab,"Ospf")
        add_config_section.addTab(eigrp_tab,"Eigrp")
        add_configuration_layout.addWidget(add_config_section)
         
#----------------------------------add config section ab----------------------------------------------------------------------#
#----------------------------------remove_configuratin section tab----------------------------------------------------------#
        remove_config_section = QtGui.QTabWidget()
        global remove_static_tab_layout
        global remove_rip_tab_layout
        global remove_ospf_tab_layout
        remove_static_tab = QtGui.QWidget()
        remove_rip_tab = QtGui.QWidget()	
        remove_ospf_tab = QtGui.QWidget()
        remove_eigrp_tab = QtGui.QWidget()	
        remove_static_tab_layout = QtGui.QFormLayout(remove_static_tab)
        remove_rip_tab_layout = QtGui.QFormLayout(remove_rip_tab)
        remove_ospf_tab_layout = QtGui.QFormLayout(remove_ospf_tab)
        remove_eigrp_tab_layout = QtGui.QFormLayout(remove_eigrp_tab)
        remove_config_section.addTab(remove_static_tab,"Static")
        remove_config_section.addTab(remove_rip_tab,"Rip")
        remove_config_section.addTab(remove_ospf_tab,"Ospf")
        remove_config_section.addTab(remove_eigrp_tab,"Eigrp")
        remove_configuration_layout.addWidget(remove_config_section)
#----------------------------------remove config section ab----------------------------------------------------------------------#

#----------------------------------view_configuratin section tab----------------------------------------------------------#
        view_config_section = QtGui.QTabWidget()
        global view_static_tab_layout
        global view_rip_tab_layout
        global view_ospf_tab_layout
        view_static_tab = QtGui.QWidget()
        view_rip_tab = QtGui.QWidget()	
        view_ospf_tab = QtGui.QWidget()
        view_eigrp_tab = QtGui.QWidget()	
        view_static_tab_layout = QtGui.QFormLayout(view_static_tab)
        view_rip_tab_layout = QtGui.QFormLayout(view_rip_tab)
        view_ospf_tab_layout = QtGui.QFormLayout(view_ospf_tab)
        view_eigrp_tab_layout = QtGui.QFormLayout(view_eigrp_tab)
        view_config_section.addTab(view_static_tab,"Static")
        view_config_section.addTab(view_rip_tab,"Rip")
        view_config_section.addTab(view_ospf_tab,"Ospf")
        view_config_section.addTab(view_eigrp_tab,"Eigrp")
        view_info_layout.addWidget(view_config_section)
#----------------------------------view configuratin section ab----------------------------------------------------------------------#
				 				 
	
#------------------------------------general layout of mainwindo---------------------------------------------------------#
        general_layout = QtGui.QVBoxLayout()      #layout object
        general_layout.addWidget(section1)		   #add section1 to layout 
        self.setLayout(general_layout)
#---------------------------------------method for creating connection field----------------------------------------------# 
    def create_connection_field(self):
		global ip_address_data
		global username_data
		global usermode_data
		global enable_mode_data
		global logOutput
		ip_address_label = QtGui.QLabel("IP Address")
		ip_address_data = QtGui.QLineEdit()
		ip_address_data.setFixedSize(400,35)
		username_label = QtGui.QLabel("Username")
		username_data = QtGui.QLineEdit()
		username_data.setFixedSize(400,35);
		user_mode_label = QtGui.QLabel("Usermode Password")
		usermode_data = QtGui.QLineEdit()
		usermode_data.setEchoMode(QtGui.QLineEdit.Password)
		usermode_data.setEchoMode(QtGui.QLineEdit.Password)
		usermode_data.setFixedSize(400,35)
		enable_mode_label = QtGui.QLabel("Enablemode Passowrd")
		enable_mode_data = QtGui.QLineEdit()
		enable_mode_data.setEchoMode(QtGui.QLineEdit.Password)
		enable_mode_data.setFixedSize(400,35)
		button = QtGui.QPushButton("Connect")
		button.setFixedSize(200,35)
		logOutput = QtGui.QTextEdit("Debugging Process!!!")
		logOutput.setReadOnly(True)
		logOutput.setFixedSize(400,150);
		connection_layout.setVerticalSpacing(25)
		connection_layout.addRow(ip_address_label,ip_address_data)
		connection_layout.addRow(username_label,username_data)
		connection_layout.addRow(user_mode_label,usermode_data)
		connection_layout.addRow(enable_mode_label,enable_mode_data)
		connection_layout.addWidget(button)
		connection_layout.addWidget(logOutput)
		button.clicked.connect(self.make_connection)
		button.clicked.connect(self.add_static_config1)
		button.clicked.connect(self.add_rip_config1)
		button.clicked.connect(self.add_ospf_config1)
		button.clicked.connect(self.remove_static1)
		button.clicked.connect(self.remove_rip1)
		button.clicked.connect(self.remove_ospf1)
		button.clicked.connect(self.veiw_static1)
		button.clicked.connect(self.view_rip1)
		button.clicked.connect(self.view_ospf1)
#---------------------------------------method for creating connection field----------------------------------------------# 
#---------------------------------------method for about applicaiton------------------------------------------------------# 

    def ShowAbout(self):
		self.text_area_about = QtGui.QTextEdit("")
		self.text_area_about.setText("1:This Application is able to Configure both Cisco and Linux router Platform \n2:Python is the Programming Language\n3:Pyside is the GUI tool")
		self.text_area_about.setReadOnly(True)
		about_layout.addWidget(self.text_area_about)
		#img = QtGui.QImage('map.jpg','jpg')
        #cursor = QtGui.QTextCursor(text_area_bout.document())
        #cursor.insertImage(img)
#---------------------------------------method for about applicaiton------------------------------------------------------# 
#---------------------------------------method for make connection--------------------------------------------------------# 

    def make_connection(self):
		global remote_conn
		ip = ip_address_data .text()
		username = username_data.text()
		usermode = usermode_data.text()
		eablemode = enable_mode_data.text()
		connection_field_data = []
		connection_field_data.extend((ip,username,usermode,eablemode))
		try:
			remote_conn_pre = paramiko.SSHClient()
			remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			remote_conn_pre.connect(connection_field_data[0],port=22,username=connection_field_data[1], password=connection_field_data[2], look_for_keys=False, allow_agent=False)
			logOutput.append("SSH connection established to %s" % ip)
			remote_conn = remote_conn_pre.invoke_shell()
			remote_conn.send("enable\n")
			time.sleep(1)
			remote_conn.send(connection_field_data[3]+ "\n")
			time.sleep(1)
			remote_conn.send("configure terminal\n")
			time.sleep(0.125)
			logOutput.append("Connection successfully established!!!")
			 
			
		except:
			logOutput.append("Connection failed!!!")
#---------------------------------------method for make connection--------------------------------------------------------# 
#---------------------------------------method for add static confuration field-------------------------------------------# 

    def add_static_config1(self):
		global static_net_data
		global static_netmask_data
		global static_gateway_data
		global static_logOutput
		net_label = QtGui.QLabel("Network Address")
		static_net_data = QtGui.QLineEdit()
		static_net_data.setFixedSize(400,35)
		netmask_label = QtGui.QLabel("Netmask")
		static_netmask_data = QtGui.QLineEdit()
		static_netmask_data.setFixedSize(400,35);
		gateway_label = QtGui.QLabel("Gateway")
		static_gateway_data = QtGui.QLineEdit()
		static_gateway_data.setFixedSize(400,35);
		button = QtGui.QPushButton("Configure")
		button.setFixedSize(200,35)
		static_logOutput = QtGui.QTextEdit("Debugging Process!!!")
		static_logOutput.setReadOnly(True)
		static_logOutput.setFixedSize(400,150);
		static_tab_layout.setVerticalSpacing(25)
		static_tab_layout.addRow(net_label,static_net_data)
		static_tab_layout.addRow(netmask_label,static_netmask_data)
		static_tab_layout.addRow(gateway_label,static_gateway_data)
		static_tab_layout.addWidget(button)
		static_tab_layout.addWidget(static_logOutput)
		button.clicked.connect(self.add_static_config2)
#---------------------------------------method for add static confuration field-------------------------------------------# 
#---------------------------------------method for add static confuration-------------------------------------------------# 

    def add_static_config2(self):
		static_net = static_net_data.text()
		static_netmask = static_netmask_data.text()
		static_gateway = static_gateway_data.text()
		static_field_data = []
		static_field_data.extend((static_net,static_netmask,static_gateway))
		print(static_field_data)
		static_logOutput.append("Configuration is starting!")
		remote_conn.send("ip route {} {} {}\n".format(static_field_data[0],static_field_data[1],static_field_data[2]))
		time.sleep(0.125)
		static_logOutput.append("Configuration Finished!")
#---------------------------------------method for add static confuration-------------------------------------------------# 
#---------------------------------------method for add rip confuration field----------------------------------------------# 

    def add_rip_config1(self):
		global rip_net_data
		global rip_logOutput
		net_label = QtGui.QLabel("Network Address")
		rip_net_data = QtGui.QLineEdit()
		rip_net_data.setFixedSize(400,35)
		button = QtGui.QPushButton("Configure")
		button.setFixedSize(200,35)
		rip_logOutput = QtGui.QTextEdit("Debugging Process!!!")
		rip_logOutput.setReadOnly(True)
		rip_logOutput.setFixedSize(400,150);
		rip_tab_layout.setVerticalSpacing(25)
		rip_tab_layout.addRow(net_label,rip_net_data)
		rip_tab_layout.addWidget(button)
		rip_tab_layout.addWidget(rip_logOutput)
		button.clicked.connect(self.add_rip_config2)
#---------------------------------------method for add rip confuration field----------------------------------------------# 
#---------------------------------------method for add rip confuration----------------------------------------------------# 

    def add_rip_config2(self):
		rip_net = rip_net_data.text()
		rip_field_data = []
		rip_field_data.append(rip_net)
		print(rip_field_data[0])
		rip_logOutput.append("Configuration is Starting!")
		remote_conn.send("router rip\n")
		time.sleep(0.125)
		remote_conn.send("network {}\n".format(rip_field_data[0]))
		time.sleep(0.125)
		rip_logOutput.append("Configuration is Finished!")
#---------------------------------------method for add rip confuration----------------------------------------------------# 
#---------------------------------------method for add ospf confuration field---------------------------------------------# 

    def add_ospf_config1(self):
		global ospf_net_data
		global ospf_netmask
		global osfp_process_id_data
		global osfp_area_data
		global ospf_logOutput
		net_label = QtGui.QLabel("Network Address")
		ospf_net_data = QtGui.QLineEdit()
		ospf_net_data.setFixedSize(400,35)
		netmask_label = QtGui.QLabel("Netmask")
		ospf_netmask = QtGui.QLineEdit()
		ospf_netmask.setFixedSize(400,35)
		ospf_process_id_label = QtGui.QLabel("Process ID")
		osfp_process_id_data = QtGui.QComboBox() 
		osfp_process_id_data.setFixedSize(400,35)
		for x in range(200):
			osfp_process_id_data.addItem("{}".format(x))
		ospf_area_label = QtGui.QLabel("Area")
		osfp_area_data = QtGui.QComboBox() 
		osfp_area_data.setFixedSize(400,35)
		for x in range(20):
			osfp_area_data.addItem("{}".format(x))
		button = QtGui.QPushButton("Configure")
		button.setFixedSize(200,35)
		ospf_logOutput = QtGui.QTextEdit("Debugging Process!!!")
		ospf_logOutput.setReadOnly(True)
		ospf_logOutput.setFixedSize(400,150);
		ospf_tab_layout.setVerticalSpacing(25)
		ospf_tab_layout.addRow(net_label,ospf_net_data)
		ospf_tab_layout.addRow(netmask_label,ospf_netmask)
		ospf_tab_layout.addRow(ospf_process_id_label,osfp_process_id_data)
		ospf_tab_layout.addRow(ospf_area_label,osfp_area_data)
		ospf_tab_layout.addWidget(button)
		ospf_tab_layout.addWidget(ospf_logOutput)
		button.clicked.connect(self.add_ospf_config2)
#---------------------------------------method for add ospf confuration field---------------------------------------------# 
#---------------------------------------method for add ospf confuration---------------------------------------------------# 

    def add_ospf_config2(self):
		net = ospf_net_data.text()
		netmask = ospf_netmask.text()
		process_id = osfp_process_id_data.currentText()
		area = osfp_area_data.currentText()
		ospf_field_data = []
		ospf_field_data.extend((net,netmask,process_id,area))
		ospf_logOutput.append("Configuration is Stating!")
		remote_conn.send("router ospf {}\n".format(ospf_field_data[2]))
		time.sleep(0.125)
		remote_conn.send("network {} {} area {}\n".format(ospf_field_data[0],ospf_field_data[1],ospf_field_data[3]))
		time.sleep(0.125)
		ospf_logOutput.append("Configuration is Finished!")
#---------------------------------------method for add ospf confuration----------------------------------------------------# 
#---------------------------------------method for remove static field-----------------------------------------------------# 

    def remove_static1(self):
		global remove_static_net_data
		global remove_static_netmask
		global remove_static_logOutput
		net_label = QtGui.QLabel("Network Address")
		remove_static_net_data = QtGui.QLineEdit()
		remove_static_net_data.setFixedSize(400,35)
		netmask_label = QtGui.QLabel("Netmask")
		remove_static_netmask = QtGui.QLineEdit()
		remove_static_netmask.setFixedSize(400,35)
		button = QtGui.QPushButton("Remove")
		button.setFixedSize(200,35)
		remove_static_logOutput = QtGui.QTextEdit("Debugging Process!!!")
		remove_static_logOutput.setReadOnly(True)
		remove_static_logOutput.setFixedSize(400,150);
		remove_static_tab_layout.setVerticalSpacing(25)
		remove_static_tab_layout.addRow(net_label,remove_static_net_data)
		remove_static_tab_layout.addRow(netmask_label,remove_static_netmask)
		remove_static_tab_layout.addWidget(button)
		remove_static_tab_layout.addWidget(remove_static_logOutput)
		button.clicked.connect(self.remove_static2)
#---------------------------------------method for remove static field-----------------------------------------------------# 
#---------------------------------------method for remove static-----------------------------------------------------------# 

    def remove_static2(self):
		net = remove_static_net_data.text()
		netmask = remove_static_netmask.text()
		remove_static_field_data = []
		remove_static_field_data.extend((net,netmask))
		remove_static_logOutput.append("Removing is Starting!")
		remote_conn.send("no ip route {} {}\n".format(remove_static_field_data[0],remove_static_field_data[1]))
		time.sleep(0.125)
		remove_static_logOutput.append("Rmoveing is Finished!")
#---------------------------------------method for remove static-----------------------------------------------------------# 
#---------------------------------------method for remove rip field--------------------------------------------------------# 

    def remove_rip1(self):
		global remove_rip_logOutput
		button = QtGui.QPushButton("Remove Rip")
		button.setFixedSize(200,35)
		remove_rip_logOutput = QtGui.QTextEdit("Debugging Process!!!")
		remove_rip_logOutput.setReadOnly(True)
		remove_rip_logOutput.setFixedSize(400,150);
		remove_rip_tab_layout.setVerticalSpacing(25)
		remove_rip_tab_layout.addWidget(button)
		remove_rip_tab_layout.addWidget(remove_rip_logOutput)
		button.clicked.connect(self.remove_rip2)
#---------------------------------------method for remove rip field--------------------------------------------------------# 
#---------------------------------------method for remove rip--------------------------------------------------------------# 

    def remove_rip2(self):
		 remove_rip_logOutput.append("Romoving Rip Stating!")
		 remote_conn.send("no router rip\n")
		 remove_rip_logOutput.append("Removing Rip is Finished!")
#---------------------------------------method for remove rip--------------------------------------------------------------# 
#---------------------------------------method for remove ospf field-------------------------------------------------------# 

    def remove_ospf1(self):
		global romove_osfp_process_id_data
		global remove_ospf_logOutput
		romove_ospf_process_id_label = QtGui.QLabel("Process ID")
		romove_osfp_process_id_data = QtGui.QComboBox() 
		romove_osfp_process_id_data.setFixedSize(400,35)
		for x in range(200):
			romove_osfp_process_id_data.addItem("{}".format(x))
		button = QtGui.QPushButton("Remove Ospf")
		button.setFixedSize(200,35)
		remove_ospf_logOutput = QtGui.QTextEdit("Debugging Process!!!")
		remove_ospf_logOutput.setReadOnly(True)
		remove_ospf_logOutput.setFixedSize(400,150);
		remove_ospf_tab_layout.setVerticalSpacing(25)
		remove_ospf_tab_layout.addRow(romove_ospf_process_id_label,romove_osfp_process_id_data)
		remove_ospf_tab_layout.addWidget(button)
		remove_ospf_tab_layout.addWidget(remove_ospf_logOutput)
		button.clicked.connect(self.remove_ospf2)
#---------------------------------------method for remove ospf field-------------------------------------------------------# 
#---------------------------------------method for remove ospf-------------------------------------------------------------# 

    def remove_ospf2(self):
		process_id = romove_osfp_process_id_data.currentText()
		remove_ospf_fied_data = []
		remove_ospf_fied_data.append(process_id)
		remove_ospf_logOutput.append("Removeing Ospf is Starting!")
		remote_conn.send("no router ospf {}\n".format(remove_ospf_fied_data[0]))
		remove_ospf_logOutput.append("Removing Ospf is Finished!")
#---------------------------------------method for remove ospf-------------------------------------------------------------# 
#---------------------------------------method for view static field-------------------------------------------------------# 

    def veiw_static1(self):
		global view_static_option_data
		global view_static_logOutput
		veiw_static_option_label = QtGui.QLabel("Static Options")
		view_static_option_data = QtGui.QComboBox() 
		view_static_option_data.setFixedSize(400,35)
		view_static_option_data.addItem("Static Routes")
		view_static_option_data.addItem("View Config File Setting")
		button = QtGui.QPushButton("View Setting")
		button.setFixedSize(200,35)
		view_static_logOutput = QtGui.QTextEdit("Debugging Process!!!")
		view_static_logOutput.setReadOnly(True)
		view_static_logOutput.setFixedSize(500,250);
		view_static_tab_layout.setVerticalSpacing(25)
		view_static_tab_layout.addRow(veiw_static_option_label,view_static_option_data)
		view_static_tab_layout.addWidget(button)
		view_static_tab_layout.addWidget(view_static_logOutput)
		button.clicked.connect(self.veiw_static2)
#---------------------------------------method for view static field-------------------------------------------------------# 
#---------------------------------------method for view static-------------------------------------------------------------# 

    def veiw_static2(self):
		if view_static_option_data.currentText() == 'Static Routes':
			remote_conn.send("do show ip route\n")
			time.sleep(1)
			result = remote_conn.recv(65535)
			router_config_file = open("rcf.txt","w")
			router_config_file.writelines(result)
			router_config_file.close()
			parse = CiscoConfParse('rcf.txt')
			for obj in parse.find_objects(r"^S"):
				view_static_logOutput.append(obj.text)
		elif view_static_option_data.currentText() == 'View Config File Setting':
			remote_conn.send("do terminal length 0\n")
			time.sleep(0.625)
			remote_conn.send("do show running-config\n")
			time.sleep(7)
			result = remote_conn.recv(65535)
			router_config_file = open("rcf.txt","w")
			router_config_file.writelines(result)
			router_config_file.close()
			parse = CiscoConfParse('rcf.txt')
			for obj in parse.find_objects(r"^ip route"):
				view_static_logOutput.append(obj.text)
#---------------------------------------method for view static-------------------------------------------------------------# 
#---------------------------------------method for view rip field----------------------------------------------------------# 

    def view_rip1(self):
		global view_rip_logOutput
		global view_rip_option_data
		veiw_rip_option_label = QtGui.QLabel("Rip Options")
		view_rip_option_data = QtGui.QComboBox() 
		view_rip_option_data.setFixedSize(400,35)
		view_rip_option_data.addItem("Rip Routes")
		view_rip_option_data.addItem("View Config File Setting")
		button = QtGui.QPushButton("View Setting")
		button.setFixedSize(200,35)
		view_rip_logOutput = QtGui.QTextEdit("Debugging Process!!!")
		view_rip_logOutput.setReadOnly(True)
		view_rip_logOutput.setFixedSize(500,250);
		view_rip_tab_layout.setVerticalSpacing(25)
		view_rip_tab_layout.addRow(veiw_rip_option_label,view_rip_option_data)
		view_rip_tab_layout.addWidget(button)
		view_rip_tab_layout.addWidget(view_rip_logOutput)
		button.clicked.connect(self.view_rip2)
#---------------------------------------method for view rip field----------------------------------------------------------# 
#---------------------------------------method for view rip----------------------------------------------------------------# 

    def view_rip2(self):
		if view_rip_option_data.currentText() == 'Rip Routes':
			remote_conn.send("do show ip route rip\n")
			time.sleep(1)
			result = remote_conn.recv(65535)
			for line in result.split("\n"):
				if '[120/1]' in line:
					view_rip_logOutput.append(line)
		elif view_rip_option_data.currentText() == 'View Config File Setting':
			remote_conn.send("do terminal length 0\n")
			time.sleep(0.625)
			remote_conn.send("do show running-config\n")
			time.sleep(7)
			result = remote_conn.recv(65535)
			router_config_file = open("rcf.txt","w")
			router_config_file.writelines(result)
			router_config_file.close()
			parse = CiscoConfParse('rcf.txt')
			children = parse.find_children('router rip')
			for obj in children:
				view_rip_logOutput.append(obj)
#---------------------------------------method for view rip----------------------------------------------------------------# 
#---------------------------------------method for view ospf field----------------------------------------------------------# 

    def view_ospf1(self):
		global view_ospf_option_data
		global view_ospf_logOutput
		veiw_ospf_option_label = QtGui.QLabel("Ospf Options")
		view_ospf_option_data = QtGui.QComboBox() 
		view_ospf_option_data.setFixedSize(400,35)
		view_ospf_option_data.addItem("Ospf Routes")
		view_ospf_option_data.addItem("Ospf Database")
		view_ospf_option_data.addItem("Ospf Routing Protocol Info")
		view_ospf_option_data.addItem("Ospf Config File Setting")
		button = QtGui.QPushButton("View Setting")
		button.setFixedSize(200,35)
		view_ospf_logOutput = QtGui.QTextEdit("Debugging Process!!!")
		view_ospf_logOutput.setReadOnly(True)
		view_ospf_logOutput.setFixedSize(500,250);
		view_ospf_tab_layout.setVerticalSpacing(25)
		view_ospf_tab_layout.addRow(veiw_ospf_option_label,view_ospf_option_data)
		view_ospf_tab_layout.addWidget(button)
		view_ospf_tab_layout.addWidget(view_ospf_logOutput)
		button.clicked.connect(self.view_ospf2)
#---------------------------------------method for view ospf field----------------------------------------------------------# 
#---------------------------------------method for view ospf----------------------------------------------------------# 

    def view_ospf2(self):
		 if view_ospf_option_data.currentText() == 'Ospf Routes':
			remote_conn.send("do show ip route ospf\n")
			time.sleep(1)
			result = remote_conn.recv(65535)
			for line in result.split("\n"):
				if line.startswith("O"):
					view_ospf_logOutput.append(line)
		 elif view_ospf_option_data.currentText() == 'Ospf Database':
			remote_conn.send("do show ip ospf database\n")
			time.sleep(1)
			result = remote_conn.recv(65535) 
			for line in result.split("\n"):
				if '0x8' in line or 'Age' in line:
					view_ospf_logOutput.append(line)
		 elif view_ospf_option_data.currentText() == 'Ospf Routing Protocol Info':
			remote_conn.send("do show ip protocols\n")
			time.sleep(1)
			result = remote_conn.recv(65535)
			for line in result.split("\n"):
				if 'Routing Protocol is' in line or 'Router ID' in line or 'Routing for' in line or 'area' in line:
					view_ospf_logOutput.append(line)
		 elif view_ospf_option_data.currentText() == 'Ospf Config File Setting':
			remote_conn.send("do terminal length 0\n")
			time.sleep(0.625)
			remote_conn.send(" do show running-config\n")
			time.sleep(7)
			result = remote_conn.recv(65535)
			router_config_file = open("rcf.txt","w")
			router_config_file.writelines(result)
			router_config_file.close()
			parse = CiscoConfParse('rcf.txt')
			children = parse.find_children('router ospf')
			for obj in children:
				view_ospf_logOutput.append(obj)
#---------------------------------------method for view ospf----------------------------------------------------------# 
    def linux_create_connection_field(self):
		linux_ip_address_label = QtGui.QLabel("IP Address")
		linux_ip_address = QtGui.QLineEdit()
		linux_ip_address.setFixedSize(400,35)
		linux_username_label = QtGui.QLabel("Username")
		linux_username = QtGui.QLineEdit()
		linux_username.setFixedSize(400,35);
		linux_password_label = QtGui.QLabel("Password")
		linux_password = QtGui.QLineEdit()
		linux_password.setEchoMode(QtGui.QLineEdit.Password)
		linux_password.setEchoMode(QtGui.QLineEdit.Password)
		linux_password.setFixedSize(400,35)
		button = QtGui.QPushButton("Connect")
		button.setFixedSize(200,35)
		linux_logOutput = QtGui.QTextEdit("Debugging Process!!!")
		linux_logOutput.setReadOnly(True)
		linux_logOutput.setFixedSize(400,150);
		linux_connection_layout.setVerticalSpacing(25)
		linux_connection_layout.addRow(linux_ip_address_label,linux_ip_address)
		linux_connection_layout.addRow(linux_username_label,linux_username)
		linux_connection_layout.addRow(linux_password_label,linux_password)
		linux_connection_layout.addWidget(button)
		linux_connection_layout.addWidget(linux_logOutput)
		
 		 
		 
	
		 
			
		 
		
		 
		
	 
		 

		 
		
		
		 
		
		 
		 
		
		 
		
		 
	 
		
	 
 		 
		
		 
		 
	 
		
		
		
		 
		
    
		  	 
        
#------------------------------------general layout of mainwindo---------------------------------------------------------#
		
if __name__=='__main__':        
	app = QtGui.QApplication(sys.argv) 
	frame = MainWindow() 
	frame.ShowAbout()
	frame.create_connection_field()
	frame.linux_create_connection_field()
	frame.show() 
	sys.exit(app.exec_())  
         
