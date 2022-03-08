from dataclasses import fields
import json
from django.http.response import Http404, HttpResponse, JsonResponse
from msilib.schema import ListView
from django.shortcuts import render
import requests

# Create your views here.

def publicar(request):
    token = refreshToken()
    jsonPublicar = {
            "title":"Item de test - No Ofertar",
            "category_id":"MLV436797",
            "price":33344,
            "currency_id":"USD",
            "available_quantity":10,
            "buying_mode":"buy_it_now",
            "condition":"new",
            "listing_type_id":"gold_special",
            "sale_terms":[
                {
                    "id":"WARRANTY_TYPE",
                    "value_name":"Garantía del vendedor"
                },
                {
                    "id":"WARRANTY_TIME",
                    "value_name":"90 días"
                }
            ],
            "pictures":[
                {"source":"https://elcomercio.pe/resizer/vn8p5kcVavk0Ezon09jXbiTQ6K8=/1200x1200/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/7DCAVEKVRBB6ZBLGUH6GXCIXLE.jpg"},
                {"source":"https://depor.com/resizer/_CcozFdYlDZICtg8RjRKxRQYPao=/1200x900/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/TKVN4FQRUZCLXNVG4CM2KET6W4.jpg"},
                {"source":"https://i0.wp.com/www.senpai.com.mx/wp-content/uploads/2021/10/Revelan-como-luce-Levi-Ackerman-como-una-waifu-de-Attack-on-Titan.jpg?fit=1280%2C720&ssl=1"}
            ],
            "attributes":[
                {
                    "id":"BRAND",
                    "value_name":"Marca del producto"
                },
                {
                    "id":"EAN",
                    "value_name":"7898095297749"
                }
            ]
            }
    response = requests.post(
        'https://api.mercadolibre.com/items',
        headers={'Authorization': 'Bearer ' + token},
        json=jsonPublicar
    )
    print(response.json())
    return HttpResponse(token)

def Descripcion(request):
    token = refreshToken()
    text = "VAMO A VE Lorem ipsum dolor sit amet consectetur, adipisicing elit. Excepturi, earum veritatis fuga, deleniti minus nisi praesentium a porro eos ad omnis, ut ab vel alias exercitationem voluptatibus incidunt ex dolor. Saepe rerum, ad officia commodi praesentium, hic nulla dicta deleniti enim error pariatur quisquam cumque optio. Beatae earum deleniti placeat, fuga perspiciatis nihil, odit possimus aliquid expedita fugiat quidem obcaecati. Aperiam quas qui voluptate incidunt quo? Facere deserunt excepturi omnis sapiente tempora nemo? Doloribus, iste placeat perspiciatis consequatur possimus earum est eligendi consequuntur ex voluptatum quis! Dignissimos distinctio quisquam perspiciatis. Quibusdam quia sit dignissimos et nisi, eum iusto illum illo nam assumenda possimus blanditiis alias, quisquam hic nemo facere, tenetur expedita aliquid ipsam consectetur rerum sequi fugit molestiae officiis? Maxime? Illo eos, quo voluptatem voluptatum nesciunt iure unde nihil nemo. Ullam delectus blanditiis qui. Facilis, fuga saepe necessitatibus cupiditate mollitia sapiente ut dolor maiores sed eveniet voluptatem omnis error? Nemo. Rem sequi assumenda consectetur itaque earum. Alias aliquid voluptatem facere. Sint repellat quo aliquam fuga veniam, dicta eveniet cupiditate soluta? Qui, nulla id. Delectus nihil hic sapiente! Est, reprehenderit at! Ad placeat cum, a fugit ab, aliquid enim maxime perferendis fuga, laudantium sunt quisquam at praesentium modi? Dolorum veniam ad molestiae tenetur nesciunt, qui mollitia vel aliquam quis minus itaque! Enim quo beatae obcaecati aliquid ratione tenetur officia ab rem. Tenetur omnis quaerat, sit, cupiditate ex laudantium similique quis, explicabo perferendis eveniet ipsam nihil reiciendis atque aliquid veritatis placeat corporis! Porro, pariatur sunt eaque placeat ad numquam nemo explicabo obcaecati saepe nihil sint nesciunt deleniti, consequatur doloribus, quasi minus dolor unde reprehenderit nobis sapiente provident error officia possimus eos. Ab! Dignissimos aut et amet atque libero, fugit, quaerat sed quisquam vero in beatae dolores quibusdam officiis doloremque reprehenderit, unde ex cum molestias explicabo earum velit provident eius! Exercitationem, earum inventore! Vero reiciendis laboriosam neque illo ducimus amet esse veniam. Numquam, nemo sequi. Amet enim est repudiandae asperiores ipsa reprehenderit nobis voluptatibus suscipit, eos facilis harum mollitia id veritatis ipsam perferendis! Quis veniam debitis, deserunt assumenda non culpa nulla est fuga nostrum voluptas dolor reprehenderit, placeat reiciendis cumque sit dolorum atque quas. In rem dolore, quibusdam error earum voluptatum! Quae, fugiat? Tempore doloribus ipsam aut eos laborum, accusantium, vitae provident quaerat totam ipsum itaque officiis labore minus autem quasi et corporis aliquid inventore voluptatem? Ducimus porro recusandae accusamus quos doloremque dolorum. Tenetur fugiat sed cum iure nihil adipisci autem earum dolorum dolores similique iste, officiis culpa architecto corporis recusandae est sapiente sint non saepe debitis maiores totam ducimus? Iure, quis necessitatibus! Eum itaque exercitationem corrupti mollitia perspiciatis quo alias! Repudiandae, laboriosam ad quod suscipit necessitatibus itaque modi perspiciatis error quisquam est soluta. Minus cumque facere laborum modi necessitatibus cupiditate, sunt nulla. Esse amet mollitia perspiciatis repellat possimus! Aperiam, ut non. Ad, hic? Asperiores labore saepe debitis facilis incidunt quisquam soluta odio vero. Harum suscipit natus error asperiores distinctio eaque in quo? Nostrum ducimus illo nisi voluptate rerum molestias illum blanditiis quos doloremque, eum sequi vitae iusto quam esse molestiae provident distinctio beatae voluptatibus autem, amet facere quia! Doloremque quo commodi culpa. Cupiditate quaerat itaque voluptatem animi dolore, obcaecati, hic dolor commodi non error odio. Repellendus minus nam beatae, voluptate quam non, temporibus magnam tempora quae aliquam, accusamus odit maiores culpa iste? Vero totam, veniam odit voluptatum debitis, molestiae molestias ipsam nobis esse dolorem corrupti laboriosam aperiam eligendi expedita. Provident illo, explicabo architecto laborum cupiditate exercitationem ducimus porro nam necessitatibus eligendi labore? Ea quasi voluptatem aliquam voluptate, culpa sapiente voluptatum. Deleniti nisi illo ut eius impedit voluptates at ipsa eligendi ab quae esse est, officia iusto architecto veritatis eos similique saepe quam. XD SI LO HIZO"
    jsonPublicar = {
        "plain_text":text
    }
    response = requests.post(
        'https://api.mercadolibre.com/items/MLV711348252/description',
        headers={'Authorization': 'Bearer ' + token,
                'Content-Type': 'application/json'},
        json=jsonPublicar
    )
    print(response.json())
    return HttpResponse(token) 

from django.core import serializers
def jsonArmado(request):
    armar = []
    armar.append({
        'title': 'Hola'
    })
    print(armar)
    armarJson = json.dumps(armar)
    print(armarJson)

    aList = [41, 58, 63]
    print(aList)
    jsonStr = json.dumps(aList)
    print(jsonStr)
    return HttpResponse(jsonStr)

def refreshToken():
    response = requests.post(
            'https://api.mercadolibre.com/oauth/token', 
            headers={'Accept': 'application/json', 
                'Content-Type': 'application/x-www-form-urlencoded'},
            data={'grant_type': 'refresh_token', 
                'client_id': '2223042557909195', 
                'client_secret': 'ccG704MccTgKJWbtxpBKCByXylX9W2yi', 
                'refresh_token': 'TG-621d4504d3c829001a9cddd9-1081981455'})

    a = response.json()
    token = a["access_token"]
    return token


def hola(request):
    return HttpResponse("ok")