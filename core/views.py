from django.db.models import FloatField, Sum
from django.db.models.functions import Cast
from django.views.generic import DetailView

from . import models


class Team(DetailView):
    model = models.Team

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['years'] = list(
            self.object.history.values_list('year', flat=True)
        )
        context['wins'] = list(
            self.object.history.values_list('wins', flat=True)
        )
        context['total_wins'] = self.object.history.aggregate(
            Sum('wins')
        )['wins__sum'] or 0
        context['total_losses'] = self.object.history.aggregate(
            Sum('losses')
        )['losses__sum'] or 0
        context['playoffs'] = list(
            self.object.history.filter(
                playoff_appearence=True
            ).values_list('year', flat=True)
        )
        context['playoff_wins'] = self.object.history.aggregate(
            Sum('playoff_wins')
        )['playoff_wins__sum'] or 0
        context['playoff_losses'] = self.object.history.aggregate(
            Sum('playoff_losses')
        )['playoff_losses__sum'] or 0
        context['championships'] = list(
            self.object.history.filter(
                championship=True
            ).values_list('year', flat=True)
        )
        context['runner_ups'] = list(
            self.object.history.filter(
                runner_up=True
            ).values_list('year', flat=True)
        )
        context['qbs'] = models.Player.objects.annotate(
            adp_as_float=Cast('adp', FloatField())
        ).filter(
            team=self.object,
            position='QB'
        ).order_by('adp_as_float')
        context['rbs'] = models.Player.objects.annotate(
            adp_as_float=Cast('adp', FloatField())
        ).filter(
            team=self.object,
            position='RB'
        ).order_by('adp_as_float')
        context['wrs'] = models.Player.objects.annotate(
            adp_as_float=Cast('adp', FloatField())
        ).filter(
            team=self.object,
            position='WR'
        ).order_by('adp_as_float')
        context['tes'] = models.Player.objects.annotate(
            adp_as_float=Cast('adp', FloatField())
        ).filter(
            team=self.object,
            position='TE'
        ).order_by('adp_as_float')
        context['franchises'] = models.Team.objects.all()
        return context
