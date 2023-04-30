
const navbarApp = Vue.createApp({
  data() {
    return {
      message: 'Hello Vue!',
      social_links: [
        {
          "id": 0,
          "class": ["fab", "fa-twitter"],
          "url": "/"
        },
        {
          "id": 1,
          "class": ["fab", "fa-facebook-square"],
          "url": "/"
        },
        {
          "id": 2,
          "class": ["fab", "fa-instagram"],
          "url": "/"
        },
        {
          "id": 3,
          "class": ["fab", "fa-pinterest-p"],
          "url": "/"
        }
      ]
    }
  },
  delimiters: ['[[', ']]']
});

navbarApp.mount('#navbarapp');

const tableApp = Vue.createApp({
  data() {
    return {
      activities: [
        {
          name: 'Put on a Coat',
          rightArm: 0,
          leftArm: 0
        },
        {
          name: 'Sleep on your Painful or Affected Side',
          rightArm: 0,
          leftArm: 0
        },
        {
          name: 'Wash Back / Do up a Bra in Back',
          rightArm: 0,
          leftArm: 0
        },
        {
          name: 'Manage Toileting',
          rightArm: 0,
          leftArm: 0
        },
        {
          name: 'Comb Hair',
          rightArm: 0,
          leftArm: 0
        },
        {
          name: 'Reach a High Shelf',
          rightArm: 0,
          leftArm: 0
        },
        {
          name: 'Lift 5 kg Above Shoulder',
          rightArm: 0,
          leftArm: 0
        },
        {
          name: 'Throw a Ball Overhead',
          rightArm: 0,
          leftArm: 0
        },
        {
          name: 'Do Usual Work',
          rightArm: 0,
          leftArm: 0
        },
        {
          name: 'Do Usual Sport',
          rightArm: 0,
          leftArm: 0
        }
      ]
    }
  },
  delimiters: ['[[', ']]']
});

tableApp.mount('#table_app');



const rangeofmotiontable = Vue.createApp({
  data() {
    return {
      motions: [
        {
          name: 'Forward flexion (max arm-trunk angle)',
          rightArm: "Active",
          leftArm: "Active"
        },
        {
          name: 'Ext-Rotation (Anatomical)',
          rightArm: "Active",
          leftArm: "Active"
        },
        {
          name: 'Ext-Rotation (Horizontal)',
          rightArm: "Active",
          leftArm: "Active"
        },
        {
          name: 'Int-Rotation (anatomical)',
          rightArm: "Active",
          leftArm: "Active"
        },
        {
          name: 'Cross-body adduction (Antecubital fosse to opposite acromion)',
          rightArm: "Active",
          leftArm: "Active"
        },

      ],
      options:
        [
          "Active", "Passive"
        ]
    }
  },
  delimiters: ['[[', ']]']
});

rangeofmotiontable.mount('#rangeofmotion_table');



const signtable1 = Vue.createApp({
  data() {
    return {
      signs: [
        {
          name: 'Supraspinatus / greater tuberosity tenderness',
          rightArm: 0,
          leftArm: 0
        },
        {
          name: 'AC joint tenderness',
          rightArm: 0,
          leftArm: 0
        },
        {
          name: 'Biceps tendon tenderness (or rupture)',
          rightArm: 0,
          leftArm: 0
        },
        {
          name: 'Other tenderness',
          rightArm: 0,
          leftArm: 0
        },

      ]
    }
  },
  delimiters: ['[[', ']]']
});

signtable1.mount('#sign_table1');



const signtable2 = Vue.createApp({
  data() {
    return {
      signs: [
        {
          name: 'Impingement l (passive flex in slight Int-Rotation)',
          rightArm: "Yes",
          leftArm: "Yes"
        },
        {
          name: 'Impingement ll (passive Int-Rotation with 90 flexion)',
          rightArm: "Yes",
          leftArm: "Yes"
        },
        {
          name: 'Impingement lll (90 active abd – classic painful arc)',
          rightArm: "Yes",
          leftArm: "Yes"
        },
        {
          name: 'Subacromial crepitus ',
          rightArm: "Yes",
          leftArm: "Yes"
        },

        {
          name: 'Scare – location:',
          rightArm: "Yes",
          leftArm: "Yes"
        },
        {
          name: 'Atrophy – location:',
          rightArm: "Yes",
          leftArm: "Yes"
        },
        {
          name: 'Deformity – describe:',
          rightArm: "Yes",
          leftArm: "Yes"
        },


      ],
      options:
        [
          "Yes", "No"
        ]
    }
  },
  delimiters: ['[[', ']]']
});

signtable2.mount('#sign_table2');




const instability_table1 = Vue.createApp({
  data() {
    return {
      choices: [
        {
          name: 'Anterior translatio',
          rightArm: 0,
          leftArm: 0,
        },
        {
          name: 'Posterior translation',
          rightArm: 0,
          leftArm: 0,
        },
        {
          name: 'Inferior translation (sulcus sign) ',
          rightArm: 0,
          leftArm: 0,
        },
        {
          name: 'Anterior apprehension ',
          rightArm: 0,
          leftArm: 0,
        },


      ],

    }
  },
  delimiters: ['[[', ']]']
});

instability_table1.mount('#instability_table1');



const instability_table2 = Vue.createApp({
  data() {
    return {
      choices: [
        {
          name: 'Reproduces test positive?',
          rightArm: "Yes",
          leftArm: "Yes",
        },
        {
          name: 'Voluntary instability?',
          rightArm: "Yes",
          leftArm: "Yes",
        },
        {
          name: 'Relocation test positive? ',
          rightArm: "Yes",
          leftArm: "Yes",
        },
        {
          name: 'Generalized ligamentous laxity?',
          rightArm: "Yes",
          leftArm: "Yes",
        },
        {
          name: 'Other physical findings',
          rightArm: "Yes",
          leftArm: "Yes",
        },

      ],
      options: [
        "Yes",
        "No"
      ]

    }
  },

  delimiters: ['[[', ']]']
});

instability_table2.mount('#instability_table2');



