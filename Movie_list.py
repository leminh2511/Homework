#Bai_1
def display_movie(m):
    print("Original name:",m["org_name"])
    print("Translated name:",m["trans_name"])
    print("Year:",m["year"])
    print()
def create_movie(org_name,trans_name,year):
    return {
        "org_name": org_name,
        "trans_name": trans_name,
        "year": year
        }
movie0=create_movie("The hunger game", "Dau truong sinh tu", 2016)
display_movie(movie0)

#Bai_2
def display_movie_list(m_list):
    sophim=1    
    for i in m_list:
        print("Movie#{0}".format(sophim))
        print("Original name:",i["org_name"])
        print("Translated name:",i["trans_name"])
        print("Year:",i["year"])
        print()
        sophim+=1
def create_movie(org_name,trans_name,year):
    return {
        "org_name": org_name,
        "trans_name": trans_name,
        "year": year
        }
movie_list=[]
movie0 = create_movie("The hunger games", "Đấu trường sinh tử", 2016)
movie1 = create_movie("Little Door Gods", "Tiểu Môn Thần", 2015)
movie_list.append(movie0)
movie_list.append(movie1)
display_movie_list(movie_list)

#Bai_3
def remove_movie(m_list,movie):
    m_list=m_list.pop(m_list.index(movie))
    return [m_list]
movie_list = remove_movie(movie_list,movie0)
display_movie_list(movie_list)
##Bai_4
def search_movie_by_year(m_list,year):
    list_seach=[]
    for i in m_list:
        if i["year"]==year:
            new_list.append(i)
    return  list_seach
movie_list = []
movie_list.append(create_movie("The hunger game", "Dau truong sinh tu", 2016))
movie_list.append(create_movie("Break point", "Ranh gioi chet", 2015))
movie_list.append(create_movie("Little Door Gods", "Tieu Mon Than", 2015))
movie_in_2015=search_movie_by_year(movie_list,2015)
display_movie_list(movie_in_2015)
        
            
            
    
