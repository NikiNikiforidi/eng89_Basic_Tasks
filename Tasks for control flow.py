# ## Completing tasks in class 23/6/21
# ###
# #  As a user I should be able to ask the user for the a rating, and receive back the appropriate response:
# # check for rating for this movie:
#   ## universal -> everyone can watch
#   ## pg --> General viewing, but some scenes may be unsuitable for young children
#   ## 12 -->  Films classified 12A and video works classified 12 contain material that is not generally suitable for
#   children aged under 12.
#   No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.
#   ## 15 --> No one younger than 15 may see a 15 film in a cinema.
#   ## 18 --> No one younger than 18 may see an 18 film in a cinema.

movie_rating = input("Which movie rating would yo like to check, Universal or PG?: ").title().strip()

if movie_rating == "Universal":
    print("Any age can watch, Enjoy the movie!")

if movie_rating == "Pg":
    print("General viewing, but some scenes may be unsuitable for young children")

viewer_age= int(input("How old is the viewer?:"))
if viewer_age <= 12:
           print("Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12.")
elif viewer_age <= 15:
            print("No one younger than 15 may see a 15 film in a cinema.")
elif viewer_age <= 18:
            print("No one younger than 18 may see an 18 film in a cinema.")