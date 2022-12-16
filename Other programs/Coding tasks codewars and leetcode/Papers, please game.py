

import datetime 

class Inspector(object):
    def __init__(self):
        self.country_list = {
                "Antegria": "Antegria", "Impor": "Impor", "Kolechia": "Kolechia", \
                "Obristan": "Obristan", "Republia": "Republia", "United Federation": \
                "United Federation", "Entrants": ["Antegria", "Impor", "Kolechia", \
                "Obristan", "Republia", "United Federation", "Arstotzka"], "Arstotzka": "Arstotzka"
                    }
        self.current_date = datetime.date(1982, 11, 22)
        self.allowed_country = []
        self.deny_country = []
        self.foreigners=  ["Antegria", "Impor", "Kolechia", "Obristan", \
                           "Republia", "United Federation"]
        self.Arstotzka_citizen = ["Arstotzka"]
        self.vaccinations_list = {"Arstotzka": [], "Antegria": [], "Impor": [], \
                             "Kolechia": [], "Obristan": [], "Republia": [], \
                                 "United Federation": []} # Creates a dictionary to contain all vaccinations
        self.vaccine_names = []
        
        self.documents_list = {"Arstotzka": [], "Antegria": [], "Impor": [], \
                                "Kolechia": [], "Obristan": [],"Republia": [], \
                                "United Federation": []}
        self.work_pass = False
        self.documents_name =["passport","certificate_of_vaccination", "access_permit", \
                              "grant_of_asylum", "diplomatic_authorization"]
        
    def receive_bulletin(self, bulletin):
        self.bulletin = bulletin
        self.bulletinCopy = bulletin.split('\n') #Seperates bulletin information to single ones
        self.allow_check_phrase = "Allow citizens of" #phrase
        self.deny_check_phrase = "Deny citizens of" #phrase
        self.vaccinations_check = "vaccination"
        self.remove_vaccination_phrase =  "no longer"
        self.wanted_check_phrase = "Wanted"
        self.wanted_count = 0
        
        
        self.wantedList = {}
        
        def update_allowed_country_list(bulletin = self.bulletinCopy):
            """
            Adds country to allowed list if the bulletin says so and country \
                is not already in allowed Country list to avoid duplicating. \
                    Also removes the country from deny list if it was already in
                    

            Parameters
            ----------
            bulletin : TYPE, optional
                DESCRIPTION. The default is self.bulletinCopy.

            Returns
            -------
            None.

            """
            for info in bulletin:
                """
                Run loop through bulletin to determine where to make changes
                based on information from bulletin 
                """
                if self.allow_check_phrase in info:
                    
                    
                    if "Entrants" in info:
                        self.allowed_country.extend(i for e in self.country_list \
                                                    for i in self.country_list[e] if i in info and i not in self.allowed_country)
                        for i in self.allowed_country:
                            if i in self.deny_country:
                                self.deny_country.remove(i)
                    else:
                        self.allowed_country.extend(self.country_list[e] for e in self.country_list \
                                                 if e in info and e not in self.allowed_country)
                        for i in self.allowed_country:
                            if i in self.deny_country:
                                self.deny_country.remove(i)
        def update_deny_country_list(bulletin = self.bulletinCopy):
            """
            Adds country to Denied list if the bulletin says so and is not already \
                in Denied Country list to avoid duplicating
            


            Parameters
            ----------
            bulletin : TYPE, optional
                DESCRIPTION. The default is self.bulletinCopy.

            Returns
            -------
            None.

            """
            for info in bulletin:
                """
                Run loop through bulletin to determine where to make changes
                based on information from bulletin 
                """
                if self.deny_check_phrase in info:
                    self.deny_country.extend([e for e in self.country_list \
                                                 if e in info and e not in self.deny_country])
                    for i in self.deny_country:
                            if i in self.allowed_country:
                                self.allowed_country.remove(i)
        def update_country_vaccination_list(bulletin = self.bulletinCopy):
            """
            Updates countries required vaccinations

            Parameters
            ----------
            bulletin : TYPE, optional
                DESCRIPTION. The default is self.bulletinCopy.

            Returns
            -------
            None.

            """
            def add_new_vaccine_name(info):
                if self.vaccinations_check in info:
                    """Checks to see if there is any information about vacination in bulletin
                       If True then do a further search in that specific info
                    """
                    self.info1 = info.split("require")
                    self.new_vaccine_name = self.info1[-1].split("vaccination")# Gets name of vaccine
                    self.new_vaccine_name = self.new_vaccine_name[0]
                    self.new_vaccine_name = self.new_vaccine_name.strip()
                    self.new_vaccine_name = self.new_vaccine_name.split(",")
                    for vaccine1 in self.new_vaccine_name:
                        if vaccine1 not in self.vaccine_names:
                            self.vaccine_names.append(vaccine1)
                    def update_vaccination_list():
                        if self.remove_vaccination_phrase in info:
                            """
                            Checks for remove_vaccination_phrase(no longer) in bulletin. If True
                            removes that vaccination from the mentioned coutries requirement
                            """
                            if "Entrants" in info:
                                for i in self.country_list:
                                    for e in self.vaccine_names:
                                        try:
                                            if e in info and e in self.vaccinations_list[i]:
                                                self.vaccinations_list[i].remove(e)
                                        except:
                                            pass
                            elif "Foreigners" in info:
                                for i in self.foreigners:
                                    for e in self.vaccine_names:
                                        try:
                                            if e in info and e in self.vaccinations_list[i]:
                                                self.vaccinations_list[i].remove(e)
                                        except:
                                            pass
                            else:
                                
                                for i in self.country_list:
                                    for e in self.vaccine_names:
                                        if i in info and e in info and e \
                                            in self.vaccinations_list[i]:
                                            self.vaccinations_list[i].remove(e)
                        else:
                            """
                            Checks for remove_vaccination_phrase(no longer) in bulletin. If False
                            adds the afforementioned vaccine to the requirements for the specified country
                            """
                            
                            if "Entrants" in info:
                                for i in self.country_list:
                                    for e in self.vaccine_names:
                                        try:
                                            if e in info and e not in self.vaccinations_list[i]:
                                                self.vaccinations_list[i].append(e)
                                        except:
                                            pass
                            elif "Foreigners" in info:
                                for i in self.foreigners:
                                    for e in self.vaccine_names:
                                        try:
                                            if e in info and e not in self.vaccinations_list[i]:
                                                self.vaccinations_list[i].append(e)
                                        except:
                                            pass
                            else:
                                for i in self.country_list:
                                    for e in self.vaccine_names:
                                        if i in info and e in info and e not in \
                                            self.vaccinations_list[i]:
                                                self.vaccinations_list[i].append(e)
                    update_vaccination_list()
            for info in bulletin:
                """
                Run loop through bulletin to determine where to make changes
                based on information from bulletin 
                """
                info = info
                add_new_vaccine_name(info)
                
        def update_wanted_list(bulletin = self.bulletinCopy):
            """
            Add new names to wantedlist dictionary 

            Parameters
            ----------
            bulletin : TYPE, optional
                DESCRIPTION. The default is self.bulletinCopy.

            Returns
            -------
            None.

            """
            for info in bulletin:
                """
                Run loop through bulletin to determine where to make changes
                based on information from bulletin 
                """
                if self.wanted_check_phrase in info:
                    """
                    Checks to see if there is any information about wanted in bulletin
                    If True then adds name to wantedList(dictionary)
                    """
                    
                    self.wanted_info = info.split(":")
                    self.wanted_info= self.wanted_info[-1].split()
                    for e in range(len(self.wanted_info)):
                        self.wanted_info[e] = self.wanted_info[e].strip(",")
                    
                    
                    self.wantedList[self.wanted_count] = self.wanted_info
                    self.wanted_count += 1
        def work_pass_check(bulletin = self.bulletinCopy):
            """
            Checks if Workers require work pass or not

            Parameters
            ----------
            bulletin : TYPE, optional
                DESCRIPTION. The default is self.bulletinCopy.

            Returns
            -------
            None.

            """
            for info in bulletin:
                """
                Run loop through bulletin to determine where to make changes
                based on information from bulletin 
                """
                if "Workers require" in info: 
                    self.work_pass = True
        def update_document_list(bulletin = self.bulletinCopy):
            """
            Update countries required documents

            Parameters
            ----------
            bulletin : TYPE, optional
                DESCRIPTION. The default is self.bulletinCopy.

            Returns
            -------
            None.

            """
            for info in bulletin:
                """
                Run loop through bulletin to determine where to make changes
                based on information from bulletin 
                """
                info = info
                self.document_check_phrase = self.allow_check_phrase not in info and \
                    self.deny_check_phrase not in info and self.vaccinations_check not in info and \
                        self.remove_vaccination_phrase not in info and self.wanted_check_phrase not in info
                def document(info = info):
                    if self.document_check_phrase:
                        def add_new_document():
                            self.info1 = info.split("require")
                            self.new_doc = self.info1[-1]# Gets name of vaccine
                            self.new_doc = self.new_doc.strip()
                            self.new_doc = self.new_doc.split()
                            self.new_doc = "_" .join(self.new_doc)
                            if self.new_doc not in self.documents_name:
                                self.documents_name.append(self.new_doc)
                        add_new_document()
                        for e in self.documents_name:
                            self.now = e.split("_")
                            self.now = " " .join(self.now)
                            if self.now in info:
                                if "Foreigners" in info:
                                            for j in self.foreigners:
                                                    try:
                                                        if e not in self.documents_list[j]:
                                                            self.documents_list[j].append(e)
                                                    except:
                                                        pass
                                else:
                                    for i in self.country_list:
                                        if i in info:
                                            if i == "Entrants":
                                                for j in self.country_list:
                                                        try:
                                                            if e not in self.documents_list[j]:
                                                                
                                                                self.documents_list[j].append(e)
                                                        except:
                                                            pass
                                        
                                                        pass
                                            else:
                                                if e not in self.documents_list[i]:
                                                    self.documents_list[i].append(e)
                document()    
        update_allowed_country_list()
        update_deny_country_list()
        update_country_vaccination_list()
        update_wanted_list()
        work_pass_check()       
        update_document_list()
    
                    
        
    def get_allowed_country(self):
        return self.allowed_country
    def get_deny_country(self):
        return self.deny_country
    def get_vaccination_list(self):
        return self.vaccinations_list
    def get_vaccine_names(self):
        return self.vaccine_names
    def get_wanted_list(self):
        return self.wantedList
    def get_document_list(self):
        return self.documents_list
    def inspect(self, entrant): 
        """
        Takes one parameter entrant which is a dictionary and is being inspected

        Parameters
        ----------
        entrant : TYPE
            DESCRIPTION.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
    
        self.entrant = entrant
        self.entrantDocs = []
        def return_nation(a):
            """
            returns person's nationality in their passport
            """
            if "passport" in a:
                for item in a:
                  if "NATION" in a[item]:
                    self.nation = a[item].split("\n")
                    for word in self.nation:
                        if "NATION" in word:
                            self.nation = word.split(":")
                            self.nation = self.nation[-1]
                            self.nation = self.nation.strip()
                            return self.nation
            else:
                return "Entry denied: missing required passport."
              
        self.entrant_nation = return_nation(self.entrant) #return person's nationality
        def nation_check():
            """
            Checks whether person's nation is in allowed countries or not.
            """
            result = True
            for e  in self.allowed_country:
                if self.entrant_nation != e:
                    result = False
                else:
                    result = True
                    break
            if result == False:
                return "Entry denied: citizen of banned nation."
        def check_wanted(a):
            """
            Checks if person is in wantedList, if yes Detain them
            """
            self.inWantedlist = []
            
            
            for item in a:
                if "NAME" in a[item]:
                    self.name = a[item].split("\n")
                    for word in self.name:
                        if "NAME" in word:
                            self.name = word.split(":")
                            self.name = self.name[-1]
                            self.name = self.name.strip()
                            self.name = self.name.split()
                            for e in range(len(self.name)):
                                self.name[e] = self.name[e].strip(",")
                           
                                for b in self.name:
                                    for i in self.wantedList:
                                        if b in self.wantedList[i]:
                                            self.inWantedlist.append(True)
                                        else:
                                            self.inWantedlist.append(False)
                                            
            if len(self.inWantedlist) > 0:
                if all(self.inWantedlist):
                    return "Detainment: Entrant is a wanted criminal."
        def documents_check(a):
            """
            Checks if person has all required documents else Deny them entry
            """
            for document in self.documents_list[self.entrant_nation]:
                
                if "access_permit" in document and document not in a:
                    
                    if 'diplomatic_authorization' in a:
                        if "Arstotzka" in a["diplomatic_authorization"]:
                            pass
                        else:
                            return "Entry denied: invalid diplomatic authorization."
                    elif "grant_of_asylum" in a:
                        pass
                    else:
                        return "Entry denied: missing required access permit."
                elif document not in a:
                    if document == "ID_card":
                        return "Entry denied: missing required ID card."
                    else:    
                        return "Entry denied: missing required " + document + "."
        def check_validity(a):
            """
            Checks if all documents are valid and not expired else return document \
                expired
            """
            for item in a:
                if "EXP" in a[item]:
                    self.new_date = a[item].split("\n")
                    try:
                        for word in self.new_date:
                            if "EXP" in word: 
                                self.new_date = word.split(":")
                                self.new_date = self.new_date[-1]
                                self.new_date = self.new_date.strip()
                                self.expiry_date = datetime.datetime.strptime(self.new_date, "%Y.%m.%d").date()
                                if self.expiry_date < self.current_date:
                                    if "access_permit" in item: 
                                        return "Entry denied: access permit expired."
                                    elif "grant_of_asylum" in item:
                                        return "Entry denied: grant of asylum expired."
                                    elif "work_pass" in item: 
                                        return "Entry denied: work pass expired."
                                    else:
                                        return "Entry denied: " + item + " expired."
                    except:
                        pass
        def check_id(a):
            """
            Checks if there is a mismatch between any of the details in any of the document \
                . If there is a mismatch Detain person
            """
            self.ID_num = None
            self.name_check = None
            self.nationality = None
            self.dob = None
            for item in a:
                if "ID#" in a[item]:
                    self.ID_number = a[item].split("\n")
                    for word in self.ID_number:
                        if "ID#" in word:
                            self.ID_number = word.split(":")
                            self.ID_number = self.ID_number[-1]
                            self.ID_number = self.ID_number.strip()
                            if self.ID_num == None:
                                self.ID_num = self.ID_number
                            else:
                                if self.ID_number != self.ID_num:
                                    return "Detainment: ID number mismatch."
            for item in a:
                if "NAME" in a[item]:
                    self.current_name = a[item].split("\n")
                    for word in self.current_name:
                        if "NAME" in word:
                            self.current_name = word.split(":")
                            self.current_name = self.current_name[-1]
                            self.current_name = self.current_name.strip()
                            if self.name_check == None:
                                self.name_check = self.current_name
                            else:
                                if self.name_check!= self.current_name:
                                    return "Detainment: name mismatch."
            for item in a:
                if "NATION" in a[item]:
                    self.current_nationality = a[item].split("\n")
                    for word in self.current_nationality:
                        if "NATION" in word:
                            self.current_nationality = word.split(":")
                            self.current_nationality = self.current_nationality[-1]
                            self.current_nationality = self.current_nationality.strip()
                            if self.nationality == None:
                                self.nationality = self.current_nationality
                            else:
                                if self.nationality != self.current_nationality:
                                    return "Detainment: nationality mismatch."
            for item in a:
                if "DOB" in a[item]:
                    self.current_dob = a[item].split("\n")
                    for word in self.current_dob:
                        if "DOB" in word:
                            self.current_dob = word.split(":")
                            self.current_dob = self.current_dob[-1]
                            self.current_dob = self.current_dob.strip()
                            if self.dob == None:
                                self.dob = self.current_dob
                            else:
                                if self.dob != self.current_dob:
                                    return "Detainment: date of birth mismatch."
        def vaccination_check(a):
            """
            Checks if vaccination is required for people from person's nation and \
                if True, has individual been vaccinated, if not deny them entry
            """
            if len(self.vaccinations_list[self.entrant_nation]) == 0:
                pass
            else:
                for vaccine in self.vaccinations_list[self.entrant_nation]:
                    if "certificate_of_vaccination" in a:
                        if vaccine not in a["certificate_of_vaccination"]:
                            return "Entry denied: missing required vaccination."
                    else:
                        return "Entry denied: missing required certificate of vaccination."
        def diplomatic_authorization_check(a):
            """
            Checks whether "Arstotzka" is in person's diplomatic authorization
            """
            if "diplomatic_authorization" in a:
                if "Arstotzka" in self.entrant["diplomatic_authorization"]:
                    pass
                else:
                    return "Entry denied: invalid diplomatic authorization."
        def check_worker(a):
            """
            Checks if person is a worker, if True check whether a work pass is required \
               if a work pass is required , check if person has a workpass 
            """
            if self.work_pass == True:
                for word in a.values():
                    if "WORK" in word and self.work_pass == True:
                        if "work_pass" in a:
                            pass
                        else:
                            return "Entry denied: missing required work pass."
        a = self.entrant
        
        if check_wanted(a) != None:
            return check_wanted(a)
        elif check_id(a) != None:
            return check_id(a)
        elif "Entry" in return_nation(self.entrant):
            return return_nation(self.entrant)
        elif nation_check() != None:
            return nation_check()
        
        
        elif documents_check(a) != None:
            return documents_check(a)
        
        elif check_validity(a) != None:
            return check_validity(a)
        
        elif vaccination_check(a) != None:
            return vaccination_check(a)
        elif diplomatic_authorization_check(a) != None:
            return diplomatic_authorization_check(a)
        elif check_worker(a) != None:
            return check_worker(a)
        elif self.entrant_nation in  self.Arstotzka_citizen:
            return "Glory to Arstotzka."
        else:
            return "Cause no trouble."
                    
            
                            
                            
                
                    
                    
                    
            
        
        
