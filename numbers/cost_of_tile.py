__author__ = 'Ranjith'

if __name__ == "__main__":

   cost_per_pack = float(raw_input("Enter cost of 1 pack of tiles : ").strip())
   area_per_pack = float(raw_input("Enter area covered by 1 pack of tiles : ").strip())
   total_width = float(raw_input("Enter total width of your floor : ").strip())
   total_height = float(raw_input("Enter total height of your floor : ").strip())

   total_area = total_width * total_height
   total_cost = (total_area * cost_per_pack) / area_per_pack

   print "Total area of your floor : %d" %total_area
   print "Total cost of your floor : %.2f" %total_cost