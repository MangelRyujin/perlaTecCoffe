from django.db import models

# Create your models here.

class Local(models.Model):
    
    local_name = models.CharField('Local name', max_length=255, blank=False , null=False, unique=True)
    active = models.BooleanField( default=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Local."""

        verbose_name = 'Local'
        verbose_name_plural = 'Locals'

    def __str__(self):
        """Unicode representation of Local."""
        return f'{self.local_name}'



class Lounge(models.Model):
    
    lounge_name = models.CharField('Lounge name', max_length=255, blank=False , null=False)
    local = models.ForeignKey(Local, on_delete=models.CASCADE,related_name='loungeLocal', verbose_name=f'Local',blank=False, null= False)
    active = models.BooleanField( default=True)
    # Define fields here

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Lounge'
        verbose_name_plural = 'Lounge'

    def __str__(self):
        """Unicode representation of Lounge."""
        return f'Local {self.local.local_name}: {self.lounge_name}'


class Table(models.Model):
    """Model definition for Table."""
    STATE_CHOICES = (
        ('busy', 'busy'),
        ('available', 'available'),
        # Add other state types here
    )

    state = models.CharField('Table state',max_length=10, choices=STATE_CHOICES, default='available') 
    number = models.PositiveIntegerField('Table number',blank=False , null=False)
    active = models.BooleanField( default=True)
    lounge = models.ForeignKey(Lounge, on_delete=models.CASCADE,related_name='tableLounge', verbose_name='Lounge',blank=False, null= False)
    max_people = models.PositiveIntegerField('Maximum number of people',default=1,blank=False , null=False)
    #  Define fields here

    class Meta:
        """Meta definition for Table."""

        verbose_name = 'Table'
        verbose_name_plural = 'Tables'

    def __str__(self):
        return f'id: {self.id}. Local {self.lounge.local.local_name}. Lounge {self.lounge.lounge_name} table #{self.number} '
