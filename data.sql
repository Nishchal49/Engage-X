INSERT INTO "main"."user" ("id", "username", "email", "role", "password", "is_flagged") VALUES ('3', 'admin', 'admin@gmail.com', 'admin', 'admin123', '0');
INSERT INTO "main"."user" ("id", "username", "email", "role", "password", "is_flagged") VALUES ('1', 'Kanika16', 'xyz@gmail.com', 'influencer', '12345678', '0');
INSERT INTO "main"."user" ("id", "username", "email", "role", "password", "is_flagged") VALUES ('5', 'raj69', 'raj@hotmail.com', 'influencer', 'rajnath01', '0');
INSERT INTO "main"."user" ("id", "username", "email", "role", "password", "is_flagged") VALUES ('6', 'kajal14', 'kaj14@gmail.com', 'influencer', 'arora489', '0');
INSERT INTO "main"."user" ("id", "username", "email", "role", "password", "is_flagged") VALUES ('7', 'riteeka07', 'rits@yahoo.com', 'influencer', 'gulanepa07', '0');
INSERT INTO "main"."user" ("id", "username", "email", "role", "password", "is_flagged") VALUES ('12', 'new_user1', 'new@gmail.com', 'influencer', 'asdfghjk', '1');
INSERT INTO "main"."user" ("id", "username", "email", "role", "password", "is_flagged") VALUES ('2', 'Anna', 'abc@gmail.com', 'sponsor', 'qwertyuio', '0');
INSERT INTO "main"."user" ("id", "username", "email", "role", "password", "is_flagged") VALUES ('4', 'ayush14', 'ayu@gmail.com', 'sponsor', 'ayu12345', '0');
INSERT INTO "main"."user" ("id", "username", "email", "role", "password", "is_flagged") VALUES ('8', 'philipy', 'philips@hotmail.com', 'sponsor', 'lightshigh', '0');
INSERT INTO "main"."user" ("id", "username", "email", "role", "password", "is_flagged") VALUES ('9', 'rapidy', 'rapids@gmail.com', 'sponsor', 'fastfast', '0');
INSERT INTO "main"."user" ("id", "username", "email", "role", "password", "is_flagged") VALUES ('10', 'oreobisk8', 'oreofamiy@gmail.com', 'sponsor', 'lick-dip-eat', '0');
INSERT INTO "main"."user" ("id", "username", "email", "role", "password", "is_flagged") VALUES ('11', 'yonekxx', 'yowaimo@gmail.com', 'sponsor', 'gosatojo', '0');
INSERT INTO "main"."user" ("id", "username", "email", "role", "password", "is_flagged") VALUES ('13', 'new_user2', 'new2@gmail.com', 'sponsor', 'zxcvbnml', '1');



INSERT INTO "main"."profile" ("id", "user_id", "name", "industry", "niche", "reach", "funds") VALUES ('1', '1', 'Kanika', 'Gaming', 'E-sports', '80000', '');
INSERT INTO "main"."profile" ("id", "user_id", "name", "industry", "niche", "reach", "funds") VALUES ('2', '2', 'Ritanch', 'Gaming', 'Gaming Equipments', '', '100000.0');
INSERT INTO "main"."profile" ("id", "user_id", "name", "industry", "niche", "reach", "funds") VALUES ('4', '4', 'Ayush', 'Beverages', 'Alcohol', '', '5000000.0');
INSERT INTO "main"."profile" ("id", "user_id", "name", "industry", "niche", "reach", "funds") VALUES ('5', '5', 'Raj', 'Electronic gadgets', 'Gadget Reviews', '15000', '');
INSERT INTO "main"."profile" ("id", "user_id", "name", "industry", "niche", "reach", "funds") VALUES ('6', '6', 'Kajal', 'Cosmetics', 'Beautician', '25000', '');
INSERT INTO "main"."profile" ("id", "user_id", "name", "industry", "niche", "reach", "funds") VALUES ('7', '7', 'Riteeka', 'Fitness', 'Gymn', '45000', '');
INSERT INTO "main"."profile" ("id", "user_id", "name", "industry", "niche", "reach", "funds") VALUES ('8', '8', 'Philips', 'Electronic Gadgets', 'Lighting', '', '30000.0');
INSERT INTO "main"."profile" ("id", "user_id", "name", "industry", "niche", "reach", "funds") VALUES ('9', '9', 'Rapidz', 'Delivery', 'Food Delivery', '', '25000.0');
INSERT INTO "main"."profile" ("id", "user_id", "name", "industry", "niche", "reach", "funds") VALUES ('10', '10', 'Oreo', 'Food', 'Packaged Products', '', '90000.0');
INSERT INTO "main"."profile" ("id", "user_id", "name", "industry", "niche", "reach", "funds") VALUES ('11', '11', 'Yonex', 'Sports', 'Badminton', '', '120000.0');
INSERT INTO "main"."profile" ("id", "user_id", "name", "industry", "niche", "reach", "funds") VALUES ('12', '12', 'test1', 'Food', 'Beverages', '51000', '');
INSERT INTO "main"."profile" ("id", "user_id", "name", "industry", "niche", "reach", "funds") VALUES ('13', '13', 'test2', 'Random', 'Troll', '', '53000.0');



INSERT INTO "main"."campaign" ("id", "sponsor_id", "title", "description", "goals", "start_date", "days", "funds", "visibility") VALUES ('1', '4', 'Motto Mastermind', 'Motto Mastermind aims to revolutionize the soda water and alcohol industry by promoting creative and inspiring slogans that resonate with modern consumers. Through a strategic roadmap focused on engaging social media campaigns and experiential marketing, we aim to elevate brand recognition and consumer loyalty', 'To establish Motto Mastermind as the leading platform for innovative branding in the soda water and alcohol industry, driving a 20% increase in brand awareness and engagement within six months.', '2024-06-30', '30', '65000.0', 'public');
INSERT INTO "main"."campaign" ("id", "sponsor_id", "title", "description", "goals", "start_date", "days", "funds", "visibility") VALUES ('2', '2', 'Pitch Planner', 'Pitch Planner introduces a comprehensive toolset designed to streamline game development pitches and proposals. Targeted at developers, studios, and investors, this campaign aims to enhance efficiency and clarity in pitching processes, facilitating smoother project approvals and collaborations within the gaming ecosystem.', 'To become the preferred choice for game developers and studios worldwide, achieving a 30% increase in user adoption and a 15% rise in successful funding pitches within the first year.', '2024-06-13', '50', '100000.0', 'public');
INSERT INTO "main"."campaign" ("id", "sponsor_id", "title", "description", "goals", "start_date", "days", "funds", "visibility") VALUES ('4', '9', 'Momentum Machine', 'Momentum Machine propels Rapidz into the forefront of the delivery industry with a focus on efficiency and customer satisfaction. This campaign introduces cutting-edge logistics solutions and seamless delivery experiences, leveraging advanced technology to redefine speed and reliability in package transportation.', 'To position Rapidz as the premier choice for fast and dependable delivery services, achieving a 30% increase in delivery speed and a 20% rise in customer retention rates within the first six months of deployment.', '2024-07-01', '40', '90000.0', 'public');
INSERT INTO "main"."campaign" ("id", "sponsor_id", "title", "description", "goals", "start_date", "days", "funds", "visibility") VALUES ('5', '9', 'Growth Guru', 'Growth Guru signifies Rapidz''s commitment to becoming a transformative force in the delivery industry. This campaign focuses on scaling operations through innovative logistics solutions and customer-centric service enhancements. By leveraging data-driven insights and strategic partnerships, Rapidz aims to optimize delivery efficiency and exceed customer expectations.', 'To solidify Rapidz''s position as a market leader in the delivery industry, achieving a 40% increase in delivery volumes and a 25% improvement in delivery reliability metrics within the first year of the campaign.', '2024-06-12', '100', '500000.0', 'public');
INSERT INTO "main"."campaign" ("id", "sponsor_id", "title", "description", "goals", "start_date", "days", "funds", "visibility") VALUES ('6', '10', 'Blitz', 'Blitz by Oreo ignites a flavor revolution in the food industry with its dynamic campaign. Designed to captivate taste buds and celebrate indulgence, Blitz introduces exciting new flavors and interactive culinary experiences. This campaign aims to engage consumers through innovative product launches and immersive digital engagements.', 'To establish Oreo Blitz as the go-to choice for adventurous food enthusiasts, achieving a 30% increase in product sales and a 20% growth in social media engagement within the first six months of launch.', '2024-05-03', '50', '60000.0', 'private');
INSERT INTO "main"."campaign" ("id", "sponsor_id", "title", "description", "goals", "start_date", "days", "funds", "visibility") VALUES ('7', '11', 'Buzz Builder', 'Buzz Builder by Yonex sets the stage for a dynamic evolution in sports equipment. This campaign is dedicated to unveiling groundbreaking innovations and enhancing performance in sports gear. Through strategic partnerships and engaging athlete endorsements, Buzz Builder aims to inspire athletes and enthusiasts alike, redefining excellence in sports equipment.', 'To establish Yonex as a trailblazer in sports equipment innovation, achieving a 25% increase in market share and a 15% rise in brand awareness among professional athletes within the first year of launch.', '2024-06-25', '30', '55000.0', 'private');
INSERT INTO "main"."campaign" ("id", "sponsor_id", "title", "description", "goals", "start_date", "days", "funds", "visibility") VALUES ('8', '8', 'Identity Impact', 'Identity Impact by Philips redefines personalization in electronics. This campaign introduces cutting-edge technologies that empower users to customize their electronic devices to reflect their unique lifestyles and preferences. Through intuitive user interfaces and sustainable design practices, Identity Impact aims to create lasting impressions and meaningful connections with consumers.', 'To position Philips as a pioneer in personalized electronics, achieving a 30% increase in product customization adoption and a 20% improvement in customer satisfaction scores within the first year of launch.', '2023-09-07', '200', '85000.0', 'private');
INSERT INTO "main"."campaign" ("id", "sponsor_id", "title", "description", "goals", "start_date", "days", "funds", "visibility") VALUES ('9', '4', 'Essence Echo', 'Essence Echo amplifies the essence of craft in alcohol and soda water, celebrating unique flavors and artisanal craftsmanship. This campaign introduces a curated selection of premium beverages that embody sophistication and distinctive taste profiles. Through experiential tastings and storytelling, Essence Echo aims to enchant consumers and elevate their drinking experience.', 'To establish Essence Echo as the preferred choice for connoisseurs seeking refined flavors and craftsmanship in alcohol and soda water, achieving a 25% increase in market share and a 15% growth in brand loyalty within the first year of launch.', '2023-12-02', '40', '65000.0', 'public');
INSERT INTO "main"."campaign" ("id", "sponsor_id", "title", "description", "goals", "start_date", "days", "funds", "visibility") VALUES ('10', '8', 'Trend Trail', 'Trend Trail by Philips leads the charge in identifying and setting trends in the consumer electronics industry. This campaign showcases Philips'' commitment to innovation and user-centric design through the introduction of cutting-edge technologies that anticipate and respond to emerging consumer needs. By fostering industry trends and setting new standards, Trend Trail aims to reshape the future of consumer electronics.', 'To establish Philips as a trendsetter in the consumer electronics industry, achieving a 30% increase in market adoption of innovative products and a 20% rise in industry recognition for trendsetting within the first year of launch.', '2023-10-12', '25', '85000.0', 'public');
INSERT INTO "main"."campaign" ("id", "sponsor_id", "title", "description", "goals", "start_date", "days", "funds", "visibility") VALUES ('11', '2', 'Game-a-thon: Level Up Your Gaming Skills!', 'Get ready for pulse-pounding action, epic battles, and adrenaline-fueled challenges at Game-a-thon! Whether you’re a seasoned gamer or a newbie, this event is your passport to a world of virtual excitement. Dive into multiplayer showdowns, explore immersive game worlds, and compete for glory. Don’t miss out—register now and let the games begin! 🕹️🔥', 'At Game-a-thon, our mission is to create an unforgettable gaming experience. We’re all about community building—bringing gamers together, fostering connections, and building camaraderie. Through workshops, challenges, and thrilling competitions, we aim to enhance players’ skills and ignite their passion for gaming. But it’s not just about fun and adrenaline; it’s also about making a difference. By channeling the event’s proceeds toward a worthy cause, we’re turning our love for games into positive impact.', '2024-07-17', '60', '60000.0', 'public');



INSERT INTO "main"."ad_request" ("id", "influencer_id", "campaign_id", "initiator", "name", "messages", "requirements", "payment_amount", "status") VALUES ('1', '7', '1', 'influencer', 'Sample title', 'Hey Motto Mastermind Team,
I''''m Riteeka, a fitness influencer passionate about inspiring others to achieve their health goals. I see a great synergy between our focus on motivation. Let''''s collaborate to create impactful content and challenges that inspire positive lifestyle changes.

Looking forward to hearing from you!', '', '15000.0', 'Pending');
INSERT INTO "main"."ad_request" ("id", "influencer_id", "campaign_id", "initiator", "name", "messages", "requirements", "payment_amount", "status") VALUES ('2', '1', '2', 'sponsor', 'Request_bySponsor1', 'Hi Kanika,

We are excited to collaborate with you on our latest gaming campaign. Your expertise and reach in the gaming community make you the perfect fit for promoting our new product.', 'Create a dedicated YouTube video reviewing our latest game.
Post a teaser video on your Instagram and Twitch accounts.
Share a series of tweets highlighting key features and your experience with the game.
Host a live-streaming session playing the game and interacting with your audience.', '20000.0', 'Pending');
INSERT INTO "main"."ad_request" ("id", "influencer_id", "campaign_id", "initiator", "name", "messages", "requirements", "payment_amount", "status") VALUES ('3', '1', '1', 'influencer', 'sample', 'Want to work ', '', '14000.0', 'Pending');
INSERT INTO "main"."ad_request" ("id", "influencer_id", "campaign_id", "initiator", "name", "messages", "requirements", "payment_amount", "status") VALUES ('4', '1', '1', 'influencer', 'Promotion together', 'Hey let me do promotion for u', '', '12000.0', 'Pending');
INSERT INTO "main"."ad_request" ("id", "influencer_id", "campaign_id", "initiator", "name", "messages", "requirements", "payment_amount", "status") VALUES ('5', '1', '1', 'sponsor', 'Nishchal', 'sdvwse r gfv rtefbv b', '', '324234.0', 'Pending');
INSERT INTO "main"."ad_request" ("id", "influencer_id", "campaign_id", "initiator", "name", "messages", "requirements", "payment_amount", "status") VALUES ('6', '1', '2', 'sponsor', 'Hey Promote Us!!', 'afwfwegf weg wreg vegvgw ev', 'rgv g wevsdg wevsdg wevdg wdvsg wvd', '12345.0', 'Pending');
INSERT INTO "main"."ad_request" ("id", "influencer_id", "campaign_id", "initiator", "name", "messages", "requirements", "payment_amount", "status") VALUES ('7', '6', '2', 'sponsor', 'Sample ad', 'Testing', 'Anything', '1450.0', 'Pending');
INSERT INTO "main"."ad_request" ("id", "influencer_id", "campaign_id", "initiator", "name", "messages", "requirements", "payment_amount", "status") VALUES ('8', '1', '11', 'influencer', 'Sample ad2', 'Hello', '', '1234.0', 'Pending');