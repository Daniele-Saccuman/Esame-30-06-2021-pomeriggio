from database.DB_connect import DBConnect
from model.Gene import Genes


class DAO():

    @staticmethod
    def getAllLocalization():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select distinct localization
                           from classification c"""
            cursor.execute(query)

            for row in cursor:
                result.append(row["localization"])

            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def getAllConnectedLocalizations():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select c1.Localization as Loc1, c2.Localization as Loc2, count(distinct i.`Type`) as peso
                    from classification c1, classification c2, interactions i 
                    where c1.Localization <> c2.Localization 
                    and c1.GeneID = i.GeneID1 
                    and c2.GeneID = i.GeneID2
                    group by Loc1, Loc2"""

        cursor.execute(query)


        for row in cursor:
            result.append((row["Loc1"], row["Loc2"], row["peso"]))

        cursor.close()
        conn.close()
        return result


