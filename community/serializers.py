from rest_framework import serializers

from .models import Community, CommunityContacts, CommunityLeadership, CommunityLeadershipType,\
                    CommunityPicture, CommunitySchools, CommunityBiomes, CommunityBiomesPicture


class CommunityLeadershipTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommunityLeadershipType
        fields = ('description',)


class CommunityLeadershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommunityLeadership
        fields = ('name', 'phone', 'type')


class CommunityContactsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommunityContacts
        fields = ('name', 'phone', 'contact_type')


class CommunityPictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommunityPicture
        fields = ('name', 'image', 'community')


class CommunitySchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommunitySchools
        fields = ('name', 'levels', 'community')


class CommunityBiomesPictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommunityBiomesPicture
        fields = ('name', 'image', 'biome')


class CommunityBiomesSerializer(serializers.ModelSerializer):

    images = CommunityBiomesPictureSerializer(many=True)

    class Meta:
        model = CommunityBiomes
        fields = ('characteristics', 'type', 'threatened_species', 'phytophysionomy', 'ground_type',
                  'images')


class CommunitySerializer(serializers.ModelSerializer):

    leadership = CommunityLeadershipSerializer(many=True)
    contacts = CommunityContactsSerializer(many=True)
    images = CommunityPictureSerializer(many=True)
    schools = CommunitySchoolSerializer(many=True)
    biomes = CommunityBiomesSerializer(many=True)

    class Meta:
        model = Community
        fields = ('name', 'geo_lat', 'geo_long', 'distance_from_capital',
                  'idh_state', 'idh_city', 'energy_type', 'families_number',
                  'religion', 'traditional_culture', 'craftwork', 'traditional_events',
                  'sanctuaries', 'hospitals_number', 'ready_care_number', 'psf_number',
                  'address', 'leadership', 'products', 'contacts', 'images', 'schools',
                  'biomes')
