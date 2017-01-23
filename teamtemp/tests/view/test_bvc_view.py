from django.core.urlresolvers import reverse
from django.test import TestCase

from teamtemp.tests.factories import TeamTemperatureFactory, TemperatureResponseFactory, TeamFactory

class BvcViewTestCases(TestCase):
    def setUp(self):
        self.teamtemp = TeamTemperatureFactory()
        self.team = TeamFactory(request=self.teamtemp)
        self.response = TemperatureResponseFactory(request=self.teamtemp, team_name=self.team.team_name)

    def test_bvc_view(self):
        response = self.client.get(reverse('bvc', kwargs={'survey_id': self.teamtemp.id}))
        self.assertTemplateUsed(response, 'bvc.html')
        self.assertEqual(response.status_code, 200)

    def test_bvc_team_view(self):
        response = self.client.get(reverse('bvc', kwargs={'survey_id': self.teamtemp.id, 'team_name': self.team.team_name}))
        self.assertTemplateUsed(response, 'bvc.html')
        self.assertEqual(response.status_code, 200)
