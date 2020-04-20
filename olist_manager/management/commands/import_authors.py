from django.core.management.base import BaseCommand, CommandError
from olist_backend.models.author import Author
import sys
import csv

class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument('args', nargs='*')

    help = "This command import authors of CSV file to database"
    
    def handle(self, *args, **options):
        if len(args) != 1:
            raise CommandError('Number of arguments invalids. Two arguments required.')
        elif '.csv' not in sys.argv[2]:
            raise CommandError('Arguments need CSV file. Check if you forgotten insert .csv extension in argument.')
        else:
            try:
                with open(sys.argv[2], mode='r') as file:
                    reader = csv.reader(file)
                    data = list(reader)
                    file.close()
            except:
                raise CommandError("File %s doesn't exists." % sys.argv[2])
            header = data[0]
            if len(data) <= 1:
                raise CommandError('There is no data that can be exported in the file %s.' % sys.argv[2])
            else:
                register_count = 0
                list_already_registered = []
                for item in data[1:len(data)]:
                    if item[header.index("name")] != '':
                        if Author.objects.filter(name=item[header.index("name")]).count() >= 1:
                            list_already_registered.append(item[header.index("name")])
                        else:
                            include_data = Author(name=item[header.index("name")])
                            include_data.save()
                            register_count = register_count + 1
                self.stdout.write(self.style.SUCCESS("CSV was imported successfully. %s Authors identifieds in file. %s Author(s) registered and %s Author(s) were ignored, because they are already registered." % (len(data) - 1, register_count, len(list_already_registered))))