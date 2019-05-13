#BONUS: Please upload a script with a user-defined function that accepts OwnerID as an input and returns 
#a vector of pet names for the given OwnerID.

#user-defined fuction (not supported in sqlite)
'''	CREATE FUNCTION [dbo].[GetPetsName](@ownderID int)
	RETURNS TABLE
	AS
	RETURN
	(
		SELECT Name 
		FROM dbo.Pets 
		WHERE ownderID = @ownderID
	);'''

	
#OR with python(using pandas dataframe)
def script(ownerID):
    return list(pets.Name.loc[pets['OwnerID'] == ownerID])