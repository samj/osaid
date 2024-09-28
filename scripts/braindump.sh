output=data/townhalls.txt
echo "Open Source Initiative (OSI) Town Hall meetings on the subject of the Open Source AI Definition (OSAID)" > $output
for i in presentations/*.txt; do
  base=$(basename -s .txt "$i")  # Get the base filename without extension
  date=$(echo "$base" | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}')  # Extract the date in YYYY-MM-DD format
  echo "### Start of next town hall held on $date ###" >> $output
  echo "--- Presentation for $date ---" >> $output
  cat "$i" >> $output  # Append the presentation content
  echo "" >> $output  # Add a blank line
  echo "--- Subtitles for $date --- ###" >> $output
  cat "townhalls/$base.txt" >> $output  # Append the corresponding subtitle
  echo "### End of last town hall held on $date ###" >> $output  # Add a separator between sections
  echo "" >> $output  # Add a blank line
done

