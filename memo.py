# Quelques noms de colonne utiles:
elig_bc_dgcl = "Eligible fraction bourg-centre selon DGCL"
elig_pq_dgcl = "Eligible fraction péréquation selon DGCL"
elig_cible_dgcl = "Eligible fraction cible selon DGCL"
code_comm = "Informations générales - Code INSEE de la commune"
nom_comm = "Informations générales - Nom de la commune"
chef_lieu_de_canton_dgcl = "Dotation de solidarité rurale Bourg-centre - Code commune chef-lieu de canton au 1er janvier 2014"

# Variables openfisca-france-dotations-locales présentes à l'état brut dans le fichier avec le nom de colonne DGCL correspondant.

variables_openfisca_presentes_fichier = {
    'bureau_centralisateur': 'Dotation de solidarité rurale Bourg-centre - Bureaux centralisateurs',
    'chef_lieu_arrondissement': "Dotation de solidarité rurale Bourg-centre - Chef-lieu d'arrondissement au 31 décembre 2014",
    'chef_lieu_de_canton': 'Dotation de solidarité rurale Bourg-centre - Code commune chef-lieu de canton au 1er janvier 2014',
    'chef_lieu_departement_dans_agglomeration': 'Dotation de solidarité rurale Bourg-centre - Chef-lieu de département agglo',
    'part_population_canton': 'Dotation de solidarité rurale Bourg-centre - Pourcentage de la population communale dans le canton',
    'population_dgf': "Informations générales - Population DGF Année N'",
    'population_dgf_agglomeration': "Dotation de solidarité rurale Bourg-centre - Population DGF des communes de l'agglomération",
    'population_dgf_departement_agglomeration': "Dotation de solidarité rurale Bourg-centre - Population départementale de référence de l'agglomération",
    'population_insee': 'Informations générales - Population INSEE Année N ',
    'potentiel_financier': 'Potentiel fiscal et financier des communes - Potentiel financier',
    'potentiel_financier_par_habitant': 'Potentiel fiscal et financier des communes - Potentiel financier par habitant',
    'revenu_total': 'Dotation de solidarité urbaine - Revenu imposable des habitants de la commune',
    'strate_demographique': 'Informations générales - Strate démographique Année N',
    'zrr': 'Dotation de solidarité rurale - Bourg-centre - Commune située en ZRR',
    'effort_fiscal': 'Effort fiscal - Effort fiscal',
    'longueur_voirie': 'Dotation de solidarité rurale - Péréquation - Longueur de voirie en mètres',
    'zone_de_montagne': 'Dotation de solidarité rurale - Péréquation - Commune située en zone de montagne',
    'insulaire': 'Dotation de solidarité rurale - Péréquation - Commune insulaire',
    'superficie': 'Informations générales - Superficie 2019',
    'population_enfants': 'Dotation de solidarité rurale - Péréquation - Population 3 à 16 ans',
    'nombre_logements': 'Dotation de solidarité urbaine - Nombre de logements TH de la commune',
    'nombre_logements_sociaux': 'Dotation de solidarité urbaine - Nombre de logements sociaux de la commune',
    'nombre_beneficiaires_aides_au_logement': 'Dotation de solidarité urbaine - Nombre de bénéficiaires des aides au logement de la commune',
    'population_qpv': 'Dotation de solidarité urbaine - Population QPV',
    'population_zfu': 'Dotation de solidarité urbaine - Population ZFU',
}

# Présente les colonnes du fichier qui représentent des variables openfisca
# résultat telles que calculées par la DGCL

variables_calculees_presentes = {
    'Dotation de solidarité rurale - Péréquation - Part Pfi (avant garantie CN)': 'dsr_fraction_perequation_part_potentiel_financier_par_habitant',
    'Dotation de solidarité rurale - Péréquation - Part VOIRIE (avant garantie CN)': 'dsr_fraction_perequation_part_longueur_voirie',
    'Dotation de solidarité rurale - Péréquation - Part ENFANTS (avant garantie CN)': 'dsr_fraction_perequation_part_enfants',
    'Dotation de solidarité rurale - Péréquation - Part Pfi/hectare (avant garantie CN)': 'dsr_fraction_perequation_part_potentiel_financier_par_hectare',
    'Dotation de solidarité rurale - Cible - Indice synthétique': 'indice_synthetique_dsr_cible',
    'Dotation de solidarité rurale - Cible - Rang DSR Cible': 'rang_indice_synthetique_dsr_cible',
    'Dotation de solidarité rurale - Cible - Part Pfi (avant garantie CN)': 'dsr_fraction_cible_part_potentiel_financier_par_habitant',
    'Dotation de solidarité rurale - Cible - Part VOIRIE (avant garantie CN)': 'dsr_fraction_cible_part_longueur_voirie',
    'Dotation de solidarité rurale - Cible - Part ENFANTS (avant garantie CN)': 'dsr_fraction_cible_part_enfants',
    'Dotation de solidarité rurale - Cible - Part Pfi/hectare (Pfis) (avant garantie CN)': 'dsr_fraction_cible_part_potentiel_financier_par_hectare',
    'Dotation de solidarité rurale Bourg-centre - Montant de la commune éligible': 'dsr_montant_eligible_fraction_bourg_centre',
    "Dotation de solidarité urbaine - Valeur de l'indice synthétique de classement de la commune à la DSU": 'indice_synthetique_dsu',
    'Dotation de solidarité urbaine - Rang de classement à la DSU des communes mét de plus de 10000 habitants': 'rang_indice_synthetique_dsu_seuil_haut',
    'Dotation de solidarité urbaine - Rang de classement à la DSU des communes mét de 5000 à 9999 habitants': 'rang_indice_synthetique_dsu_seuil_bas',
    'Dotation de solidarité urbaine - Montant de la garantie effectivement appliquée à la commune': 'dsu_montant_garantie_non_eligible',
    'Dotation de solidarité urbaine - Montant attribution spontanée DSU': 'dsu_part_spontanee',
    'Dotation de solidarité urbaine - Montant progression de la DSU': 'dsu_part_augmentation',
    'Dotation de solidarité urbaine - Montant total réparti': 'dsu_montant',
    'Dotation de solidarité rurale Bourg-centre - Montant global réparti': 'dsr_fraction_bourg_centre',
    'Dotation de solidarité rurale - Péréquation - Montant global réparti (après garantie CN)': 'dsr_fraction_perequation',
    'Dotation de solidarité rurale - Cible - Montant global réparti': 'dsr_fraction_cible',
}


# Présente les colonnes du fichier qui représentent des variables openfisca
variables_calculees_an_dernier = {
    'Dotation de solidarité rurale Bourg-centre - Montant de la commune éligible': 'dsr_montant_eligible_fraction_bourg_centre',
    'Dotation de solidarité urbaine - Montant attribution spontanée DSU': 'dsu_part_spontanee',
    'Dotation de solidarité urbaine - Montant progression de la DSU': 'dsu_part_augmentation',
    'Dotation de solidarité urbaine - Montant total réparti': 'dsu_montant',
    'Dotation de solidarité rurale - Cible - Part Pfi (avant garantie CN)': 'dsr_fraction_cible_part_potentiel_financier_par_habitant',
    'Dotation de solidarité rurale - Cible - Part VOIRIE (avant garantie CN)': 'dsr_fraction_cible_part_longueur_voirie',
    'Dotation de solidarité rurale - Cible - Part ENFANTS (avant garantie CN)': 'dsr_fraction_cible_part_enfants',
    'Dotation de solidarité rurale - Cible - Part Pfi/hectare (Pfis) (avant garantie CN)': 'dsr_fraction_cible_part_potentiel_financier_par_hectare',
    'Dotation de solidarité rurale - Péréquation - Part Pfi (avant garantie CN)': 'dsr_fraction_perequation_part_potentiel_financier_par_habitant',
    'Dotation de solidarité rurale - Péréquation - Part VOIRIE (avant garantie CN)': 'dsr_fraction_perequation_part_longueur_voirie',
    'Dotation de solidarité rurale - Péréquation - Part ENFANTS (avant garantie CN)': 'dsr_fraction_perequation_part_enfants',
    'Dotation de solidarité rurale - Péréquation - Part Pfi/hectare (avant garantie CN)': 'dsr_fraction_perequation_part_potentiel_financier_par_hectare',
    'Dotation de solidarité rurale Bourg-centre - Montant global réparti': 'dsr_fraction_bourg_centre',
    'Dotation de solidarité rurale - Péréquation - Montant global réparti (après garantie CN)': 'dsr_fraction_perequation',
    'Dotation de solidarité rurale - Cible - Montant global réparti': 'dsr_fraction_cible',
}
