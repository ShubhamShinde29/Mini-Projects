insert_query="""insert into stud(fname,lname,Mob,email,uname,pass,que,ans)values(%s, %s, %s, %s, %s, %s, %s, %s)"""
                        cur.execute(insert_query,record)
                        con.commit()